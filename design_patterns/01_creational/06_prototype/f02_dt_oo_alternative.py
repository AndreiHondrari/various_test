
import copy
import random


class X:

    def __init__(self) -> None:
        self.bla = random.randint(900, 1000)

    def __str__(self) -> str:
        return f"X({id(self)})[bla: {self.bla}]"


class A:

    def __init__(self) -> None:
        self.field1 = random.randint(1, 100 + 1)
        self.x = X()

    def __str__(self) -> str:
        return f"A({id(self)})[field1: {self.field1}, x: {str(self.x)}]"


class B(A):

    def __init__(self) -> None:
        super().__init__()
        self.field2 = random.randint(101, 200 + 1)

    def __str__(self) -> str:
        return f"B({id(self)})[field2: {self.field2}] {super().__str__()}"


if __name__ == "__main__":
    # main class clone
    a1 = A()
    print(f"a1 {id(a1)}: {a1}")

    a2 = copy.copy(a1)
    print(f"a2 {id(a2)}: {a2} (shallow)")

    a3 = copy.deepcopy(a1)
    print(f"a3 {id(a3)}: {a3} (deep)")

    # subclass clone
    b1 = B()
    print(f"b1 {id(b1)}: {b1}")

    b2 = copy.copy(b1)
    print(f"b2 {id(b2)}: {b2} (shallow)")

    b3 = copy.deepcopy(b1)
    print(f"b3 {id(b3)}: {b3} (deep)")
