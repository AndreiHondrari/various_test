#!python

import sys
import socket
import signal
import types

DEFAULT_HOST_NAME = "localhost"
DEFAULT_PORT = 54321
NO_OF_UNACCEPTED_CONNECTIONS = 5

if __name__ == "__main__":

    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host_addr = socket.gethostbyname(DEFAULT_HOST_NAME)
    server_socket.bind((host_addr, DEFAULT_PORT))

    def sigint_handler(
        sig: signal.Signals,
        frame: types.FrameType,
    ) -> None:
        print("\n\nYou pressed Ctrl+C")
        server_socket.close()
        print("Listening stopped.")
        sys.exit(0)

    signal.signal(signal.SIGINT, sigint_handler)

    print("Listening on {}:{}\n".format(host_addr, DEFAULT_PORT))
    server_socket.listen(NO_OF_UNACCEPTED_CONNECTIONS)

    while True:
        server_connection, addr = server_socket.accept()

        try:
            while True:
                data = server_connection.recv(1024).decode()

                if data == "":
                    break

                print("{}: {}".format(addr, data))
        except socket.error:
            break
