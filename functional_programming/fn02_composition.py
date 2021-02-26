"""
Composition, output of a function as input to another function
"""


def add(a: int, b: int) -> int:
    return a + b


def duplicate(x: int) -> int:
    return x * 2


if __name__ == "__main__":
    x: int = add(11, 22)
    y: int = duplicate(x)
    print(f"Y: {y}")

    z: int = duplicate(add(11, 22))
    print(f"Z: {z}")
