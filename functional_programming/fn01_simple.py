"""
Simplest form, value in, value out
"""


def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    x: int = add(11, 22)
    print(f"X: {x}")
