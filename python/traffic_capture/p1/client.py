#!python

import sys
import socket
import signal
import types

DEFAULT_HOST_NAME = "localhost"
DEFAULT_PORT = 54321

if __name__ == "__main__":

    def sigint_handler(
        sig: signal.Signals,
        frame: types.FrameType,
    ) -> None:
        print("Sending stopped.")
        sys.exit(0)

    signal.signal(signal.SIGINT, sigint_handler)

    print("Type to send to {}:{}\n".format(DEFAULT_HOST_NAME, DEFAULT_PORT))

    while True:
        data = input()

        client_socket = socket.socket()
        client_socket.connect((DEFAULT_HOST_NAME, DEFAULT_PORT))
        client_socket.settimeout(None)
        client_socket.send(data.encode())
        client_socket.close()
