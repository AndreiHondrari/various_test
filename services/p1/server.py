import aiohttp
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp')
app = aiohttp.web.Application()
sio.attach(app)


@sio.event
async def some_event(sid, data):
    print(f"{sid}: {data}")
    await sio.emit("pong", f"pongback {data}", room=sid)


@sio.event
def connect(sid, environ, auth):
    print(f"CONN: {sid}: {environ}\n--->{auth}")


@sio.event
def disconnect(sid):
    print(f"DISC: {sid}")


if __name__ == "__main__":
    aiohttp.web.run_app(
        app,
        host='localhost',
        port=54321
    )
