import asyncio
import random as rd

import socketio

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


async def loop():
    while True:
        await asyncio.sleep(1)

        x = rd.randint(0, 100)
        print(f"FFF: {x}")
        await sio.emit('some_event', f"{x}")


async def main():
    await sio.connect('http://localhost:54321')
    await loop()
    # await sio.wait()

if __name__ == "__main__":

    print("hello there\n-------------\n")

    asyncio.run(main())
