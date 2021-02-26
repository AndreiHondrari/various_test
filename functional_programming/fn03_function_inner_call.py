"""
Calling function from inside
"""


def add(a: int, b: int) -> int:
    return a + b


def duplicate(x: int) -> int:
    return x * 2


def add_and_duplicate(a: int, b: int) -> int:
    return duplicate(add(a, b))


if __name__ == "__main__":
    x: int = add_and_duplicate(11, 22)
    print(f"X: {x}")
