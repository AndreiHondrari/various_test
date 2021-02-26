"""
Higher order function, ability to return functions
"""

from typing import Callable


def add(a: int, b: int) -> int:
    return a + b


def duplicate(x: int) -> int:
    return x * 2


def create_two_inputs_to_one_output_function(
    first_function: Callable,
    second_function: Callable,
) -> int:
    """
    Notice that the set of inputs matches
    the set of inputs of the first function.
    """

    def composed_function(a: int, b: int):
        return second_function(first_function(a, b))

    return composed_function


if __name__ == "__main__":
    func = create_two_inputs_to_one_output_function(add, duplicate)
    x = func(11, 22)
    print(f"X: {x}")
