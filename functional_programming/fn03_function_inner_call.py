"""
Calling function from inside
"""

# define some primary functions
def add(a: int, b: int) -> int:
    return a + b


def duplicate(x: int) -> int:
    return x * 2


# embedded composition - intermixing external function calls with internal code

def triple_sum(a: int, b: int) -> int:
    """
    Notice how inputs of triple_sum are mapped directly to add.
    Mapping is preserved from inputs to output perfectly.
    """
    addition_result = add(a, b)
    return addition_result * 3


def double_product(a: int, b: int) -> int:
    """
    Notice how inputs don't map directly to duplicate, but instead
    they are processed into a value which is passed to duplicate.
    Mapping is preserved from inputs to output perfectly.
    """

    product_result = a * b
    return duplicate(product_result)


# decoupled composition - operating on results of outside function calls

def add_and_duplicate(a: int, b: int) -> int:
    return duplicate(add(a, b))


if __name__ == "__main__":
    m: int = triple_sum(11, 22)
    print(f"M: {m}")

    n: int = double_product(2, 3)
    print(f"N: {n}")

    x: int = add_and_duplicate(11, 22)
    print(f"X: {x}")
