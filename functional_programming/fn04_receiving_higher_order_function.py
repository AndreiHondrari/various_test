"""
Higher order function, ability to pass functions as parameters
"""

from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def duplicate(x: int) -> int:
    return x * 2


def calculate_composed(
    first_function: Callable,
    second_function: Callable,
    a: int,
    b: int
) -> int:
    return second_function(first_function(a, b))


if __name__ == "__main__":
    x: int = calculate_composed(add, duplicate, 11, 22)
    print(f"X: {x}")
