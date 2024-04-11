from . import parse_log_entry


def test_aiohttp_server():
    entry = {
        "name": "aiohttp.server",
        "message": ["Error handling request"],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/aiohttp/web_protocol.py",
            421,
        ],
        "timestamp": 1712756321.8393567,
        "exception": 'Traceback (most recent call last):\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 992, in _wrap_create_connection\n    return await self._loop.create_connection(*args, **kwargs)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 1119, in create_connection\n    raise exceptions[0]\n  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 1101, in create_connection\n    sock = await self._connect_sock(\n           ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/asyncio/base_events.py", line 1004, in _connect_sock\n    await self.sock_connect(sock, address)\n  File "/usr/local/lib/python3.12/asyncio/selector_events.py", line 637, in sock_connect\n    return await fut\n           ^^^^^^^^^\n  File "/usr/local/lib/python3.12/asyncio/selector_events.py", line 677, in _sock_connect_cb\n    raise OSError(err, f\'Connect call failed {address}\')\nConnectionRefusedError: [Errno 111] Connect call failed (\'127.0.0.1\', 443)\n\nThe above exception was the direct cause of the following exception:\n\nTraceback (most recent call last):\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/web_protocol.py", line 452, in _handle_request\n    resp = await request_handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/web_app.py", line 543, in _handle\n    resp = await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/web_middlewares.py", line 114, in impl\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/security_filter.py", line 91, in security_filter_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/forwarded.py", line 100, in forwarded_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/request_context.py", line 28, in request_context_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/ban.py", line 80, in ban_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/auth.py", line 235, in auth_middleware\n    return await handler(request)\n           ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/headers.py", line 31, in headers_middleware\n    response = await handler(request)\n               ^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/http/view.py", line 149, in handle\n    result = await handler(request, **request.match_info)\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 1255, in get\n    data, content_type = await player.async_get_media_image()\n                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 655, in async_get_media_image\n    return await self._async_fetch_image_from_cache(url)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 1174, in _async_fetch_image_from_cache\n    (content, content_type) = await self._async_fetch_image(url)\n                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 1185, in _async_fetch_image\n    return await async_fetch_image(_LOGGER, self.hass, url)\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/src/homeassistant/homeassistant/components/media_player/__init__.py", line 1350, in async_fetch_image\n    response = await websession.get(url)\n               ^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/client.py", line 578, in _request\n    conn = await self._connector.connect(\n           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 544, in connect\n    proto = await self._create_connection(req, traces, timeout)\n            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 911, in _create_connection\n    _, proto = await self._create_direct_connection(req, traces, timeout)\n               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 1235, in _create_direct_connection\n    raise last_exc\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 1204, in _create_direct_connection\n    transp, proto = await self._wrap_create_connection(\n                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n  File "/usr/local/lib/python3.12/site-packages/aiohttp/connector.py", line 1000, in _wrap_create_connection\n    raise client_error(req.connection_key, exc) from exc\naiohttp.client_exceptions.ClientConnectorError: Cannot connect to host graph.facebook.com:443 ssl:default [Connect call failed (\'127.0.0.1\', 443)]\n',
        "count": 3,
        "first_occurred": 1712756321.6496823,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "domain": "media_player",
        "name": "aiohttp.server",
        "package": "aiohttp",
        "short": "Cannot connect to host graph.facebook.com:443",
    }


def test_yandex_smart_home():
    entry = {
        "name": "custom_components.yandex_smart_home.smart_home",
        "message": [
            "INTERNAL_ERROR: Failed to execute action for instance on (devices.capabilities.on_off) of light.kids_lamp: HomeAssistantError('Error when calling _async_turn_on for bulb Yeelight Ceiling6 0x80xxxxx at 192.168.1.123: The write socket is closed')"
        ],
        "level": "ERROR",
        "source": ["custom_components/yandex_smart_home/smart_home.py", 151],
        "timestamp": 1712762773.383661,
        "exception": "",
        "count": 1,
        "first_occurred": 1712762773.383661,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "domain": "yandex_smart_home",
        "name": "custom_components.yandex_smart_home.smart_home",
        "short": "Error connect to 192.168.1.123",
    }


def test_pychromecast():
    entry = {
        "name": "pychromecast.socket_client",
        "message": [
            "[MIBOX4(192.168.1.123):8009] Heartbeat timeout, resetting connection",
        ],
        "level": "WARNING",
        "source": [
            "/usr/local/lib/python3.12/site-packages/pychromecast/socket_client.py",
            664,
        ],
        "timestamp": 1712806799.5915406,
        "exception": "",
        "count": 14,
        "first_occurred": 1712762147.9811645,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "name": "pychromecast.socket_client",
        "package": "pychromecast",
        "short": "Error connect to 192.168.1.123",
    }

    entry = {
        "name": "pychromecast.socket_client",
        "message": ["[All(192.168.1.123):32156] Error reading from socket."],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/pychromecast/socket_client.py",
            616,
        ],
        "timestamp": 1712806815.509437,
        "exception": "",
        "count": 4,
        "first_occurred": 1712799203.7723434,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "name": "pychromecast.socket_client",
        "package": "pychromecast",
        "short": "Error connect to 192.168.1.123",
    }

    entry = {
        "name": "pychromecast.socket_client",
        "message": [
            "[All(192.168.1.123):32156] Error communicating with socket, resetting connection"
        ],
        "level": "WARNING",
        "source": [
            "/usr/local/lib/python3.12/site-packages/pychromecast/socket_client.py",
            655,
        ],
        "timestamp": 1712806815.5136075,
        "exception": "",
        "count": 4,
        "first_occurred": 1712799203.7767339,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "name": "pychromecast.socket_client",
        "package": "pychromecast",
        "short": "Error connect to 192.168.1.123",
    }

    entry = {
        "name": "pychromecast.socket_client",
        "message": [
            "[All(192.168.1.123):32156] Failed to connect to service HostServiceInfo(host='192.168.1.123', port=32156), retrying in 5.0s",
        ],
        "level": "ERROR",
        "source": [
            "/usr/local/lib/python3.12/site-packages/pychromecast/socket_client.py",
            412,
        ],
        "timestamp": 1712806818.2968147,
        "exception": "",
        "count": 16,
        "first_occurred": 1712762177.9957035,
    }
    assert parse_log_entry(entry) == {
        "category": "connection",
        "name": "pychromecast.socket_client",
        "package": "pychromecast",
        "short": "Error connect to 192.168.1.123",
    }