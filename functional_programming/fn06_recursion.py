"""
Recursion
"""


def accumulate(n: int):
    return (accumulate(n - 1) + n) if n != 0 else 0


if __name__ == "__main__":
    x: int = accumulate(5)
    print(f"X {x}")
