#!python

import sys
import os
import socket
import pyshark
import enum
import signal
import types

from typing import List


@enum.unique
class TCPFlag(enum.IntEnum):
    NS = (
        0b1_0000_0000
    )
    CWR = (
        0b0_1000_0000
    )
    ECE = (
        0b0_0100_0000
    )
    URG = (
        0b0_0010_0000
    )
    ACK = (
        0b0_0001_0000
    )
    PSH = (
        0b0_0000_1000
    )
    RST = (
        0b0_0000_0100
    )
    SYN = (
        0b0_0000_0010
    )
    FIN = (
        0b0_0000_0001
    )


def main() -> None:
    running: bool = True

    localhost_if_name = socket.if_nameindex()[0][1]
    print(
        f"Sniffing interface: {localhost_if_name} "
        "(presumably it is a localhost interface)"
    )
    capture = pyshark.LiveCapture(
        interface=localhost_if_name,
        use_json=True,
        include_raw=True,
    )

    def sigint_handler(
        sig: signal.Signals,
        frame: types.FrameType,
    ) -> None:
        print("Stopped sniffing.")
        running = False  # noqa: F841

    signal.signal(signal.SIGINT, sigint_handler)

    for packet in capture.sniff_continuously():

        if not running:
            break

        print("\n##################### NEW PACKET #######################")
        tcp_layer = getattr(packet, 'tcp', None)

        print(f"Packet number: {packet.number}")
        print(f"Packet captured length: {packet.captured_length}")
        print(f"Packet layers: {packet.layers}")

        if tcp_layer is not None:
            tcp_flags = tcp_layer.flags.hex_value

            print(f"TCP seq: {tcp_layer.seq}")
            print(f"TCP syn: {tcp_flags & TCPFlag.PSH}")
            print(f"TCP ack: {tcp_layer.ack}")
            print(f"TCP stream: {tcp_layer.stream}")
            print(f"TCP flags: {tcp_flags:0>9b}")
            print(f"TCP checksum: {tcp_layer.checksum}")
            print(f"TCP srcport: {tcp_layer.srcport}")
            print(f"TCP dstport: {tcp_layer.dstport}")

            if tcp_flags & TCPFlag.PSH:
                data_hex_values: List[str] = packet.data.data.split(":")
                data_characters: List[str] = list(
                    map(
                        lambda hexval: chr(int(hexval, base=16)),
                        data_hex_values
                    )
                )
                data_string = "".join(data_characters)
                print(f"DATA: {data_string}")


if __name__ == "__main__":

    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")

        try:
            print("Sys exit")
            sys.exit(0)
        except SystemExit:
            print("OS exit")
            os._exit(0)
