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
    """
    Notice how the a and b inputs map to the first_function inputs.
    The calculate_composed is the perfect embodiment of the two functions and
    the a and b numbers, functions being part of the whole operation
    the same way as a and b are, making calculate_composed a superior function.

    It expects that:
        - first_function is a mapping of (int, int) -> int
        - second_function is a mpping of int -> int
    """
    return second_function(first_function(a, b))


if __name__ == "__main__":
    x: int = calculate_composed(add, duplicate, 11, 22)
    print(f"X: {x}")
