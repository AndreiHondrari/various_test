import asyncio
import random as rd

import socketio

from Message_pb2 import Message

sio = socketio.AsyncClient()


@sio.event
async def connect():
    print("I'm connected")


@sio.event
async def disconnect():
    print("I'm disconnected")


@sio.event
async def pong(*args, **kwargs):
    print(f"PONG: {args} ||| {kwargs}")


def process_response(*args, **kwargs):
    print(f"RESPONSE: {args} ||| {kwargs}\n")


async def loop():
    while True:

        msg = Message()
        msg.bla = f"DUMBLEDORE: {rd.randint(0, 100)}"
        msg.a1 = rd.randint(0, 100)
        msg.a2 = rd.randint(0, 100)
        msg.a3 = rd.randint(0, 100)
        msg.a4 = rd.randint(0, 100)
        msg.a5 = rd.randint(0, 100)

        print("------------------")
        print(f"FFF: {msg}")
        await sio.emit(
            'some_event',
            msg.SerializeToString(),
            callback=process_response
        )

        await asyncio.sleep(1)


async def main():
    await sio.connect('http://localhost:54321')
    await loop()

if __name__ == "__main__":

    print("hello there\n-------------\n")

    asyncio.run(main())
