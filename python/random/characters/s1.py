
import time


def main() -> None:

    MAX = 50
    for i in range(1, MAX + 1):
        dashes = "-" * i
        percentage = int(100 * i / MAX)
        line = f"[{percentage: >3}%] {dashes}>"
        print(line, end="", flush=True)
        line_length = len(line)
        time.sleep(0.025)

        # clear line
        print("\b" * line_length, end="", flush=True)
        print(" " * line_length, end="", flush=True)
        print("\b" * line_length, end="", flush=True)

    print()


if __name__ == '__main__':
    main()
