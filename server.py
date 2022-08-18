import os
import json
from aiohttp import web

WS_FILE = os.path.join(os.path.dirname(__file__), "websocket.html")

async def wshandler(request: web.Request):
    resp = web.WebSocketResponse()
    available = resp.can_prepare(request)
    if not available:
        with open(WS_FILE, "rb") as fp:
            return web.Response(body=fp.read(), content_type="text/html")

    await resp.prepare(request)

    # await resp.send_str(json.loads({'server':"Добро пожаловать!"}))

    try:
        print("Кто-то подсоединился")
        # for ws in request.app["sockets"]:
        #     await ws.send_str(json.dumps({'server':"Кто-то подсоединился"}, indent=4))
        request.app["sockets"].append(resp)

        async for msg in resp:
            if msg.type == web.WSMsgType.TEXT:
                for ws in request.app["sockets"]:
                    if ws is not resp:
                        await ws.send_str(msg.data)
            else:
                return resp
        return resp

    finally:
        request.app["sockets"].remove(resp)
        print("Кто-то отсоединился")
        # for ws in request.app["sockets"]:
        #     await ws.send_str(json.dumps({'server':"Кто-то отсоединился"}, indent=4))

async def on_shutdown(app: web.Application):
    for ws in app["sockets"]:
        await ws.close() 


def init():
    app = web.Application()
    app["sockets"] = []
    app.router.add_get("/", wshandler) 
    app.on_shutdown.append(on_shutdown)
    return app


web.run_app(init())