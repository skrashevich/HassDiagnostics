import re
import traceback
from logging import LogRecord

RE_CUSTOM_DOMAIN = re.compile(r"\bcustom_components[/.]([0-9a-z_]+)")
RE_DOMAIN = re.compile(r"\bcomponents[/.]([0-9a-z_]+)")
RE_DEPRECATED = re.compile(r"will stop working in Home Assistant.+?[0-9.]+")
RE_IS_DEPRECATED = re.compile(r"\bis deprecated\b")
RE_SETUP = re.compile(r"^Setup of ([^ ]+) is taking over")
RE_UPDATING = re.compile(r"^Updating ([^ ]+) [^ ]+ took longer than")
RE_PACKAGE = re.compile(r"/site-packages/([^/]+)")
RE_TEMPLATE = re.compile(r"Template<template=\((.+?)\) renders=", flags=re.DOTALL)
RE_CONNECT_TO_HOST = re.compile(r"Cannot connect to host ([^ :]+)")
RE_CONNECT = re.compile(
    r"\b(connect|connection|disconnected|socket|timed out)\b", flags=re.IGNORECASE
)
RE_LOGIN = re.compile(r"^Login attempt or request [^(]+\(([^)]+)")
RE_LAST_LINE = re.compile(r"\n\S+Error: ([^\n]+)\n$")


def parse_log_record(record: LogRecord) -> dict:
    message = short = record.message or record.getMessage()

    # base info
    entry = {
        "name": record.name,
        "level": record.levelname,
        "message": message,
        "timestamp": record.created,
    }

    # domain from name, message and exception
    text = f"{record.name}\n{message}\n"
    if record.exc_info:
        text += record.exc_text or str(traceback.format_exception(*record.exc_info))

    if m := RE_CUSTOM_DOMAIN.search(text):
        entry["domain"] = m[1]
    elif m := RE_DOMAIN.findall(text):
        entry["domain"] = m[-1]

    # package from pathname
    if m := RE_PACKAGE.search(record.pathname):
        entry["package"] = m[1]

    if host := ip_search(message):
        entry["host"] = host

    # short and category
    if m := RE_CONNECT_TO_HOST.search(text):
        entry["category"] = "connection"
        entry["host"] = m[1]
    elif RE_CONNECT.search(message) and entry.get("host"):
        entry["category"] = "connection"
    elif m := RE_DEPRECATED.search(message):
        entry["category"] = "deprecated"
        short = "..." + m[0]
    elif RE_IS_DEPRECATED.search(message):
        entry["category"] = "deprecated"
    elif m := RE_SETUP.search(message):
        entry["category"] = "performance"
        entry["domain"] = m[1]
    elif m := RE_UPDATING.search(message):
        entry["category"] = "performance"
        entry["domain"] = m[1]
    elif m := RE_TEMPLATE.search(message):
        entry["category"] = "template"
        short = m[1]
    elif m := RE_LOGIN.search(message):
        entry["category"] = "login"
        entry["host"] = m[1]
    elif m := RE_LAST_LINE.search(text):
        short = m[1]
        if host := ip_search(short):
            entry["host"] = host
        if RE_CONNECT.search(short) and entry.get("host"):
            entry["category"] = "connection"

    if record.name == "homeassistant.components.websocket_api.http.connection":
        short = short.lstrip("[0123456789] ")

    if len(short) > 62:
        short = short[:59] + "..."

    entry["short"] = short.replace("\n", " ")

    return entry


RE_IP = re.compile(r"\b[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\b")


def ip_search(text: str) -> str | None:
    m: list[str] = RE_IP.findall(text)
    for host in m:
        a, b, c, d = host.split(".")
        if 0 < int(a) < 255 and int(b) <= 255 and int(c) <= 255 and 0 < int(d) < 255:
            return host
    return None


def convert_log_entry_to_record(entry: dict):
    args = {
        "name": entry["name"],
        "levelname": entry["level"],
        "created": entry["timestamp"],
        "pathname": entry["source"][0],
        "message": entry["message"][0],
        "exc_info": entry["exception"] != "",
        "exc_text": entry["exception"],
    }
    return type("LogRecord", (), args)()
