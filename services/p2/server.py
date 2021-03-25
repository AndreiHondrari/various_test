import aiohttp
import socketio

from Message_pb2 import Message

sio = socketio.AsyncServer(async_mode='aiohttp')
app = aiohttp.web.Application()
sio.attach(app)


@sio.event
async def some_event(sid, data):
    decoded_message = Message()
    decoded_message.ParseFromString(data)
    print(f"{sid}: {decoded_message}")
    await sio.emit("pong", f"pongback {decoded_message.bla}", room=sid)
    return "OK", 111


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
