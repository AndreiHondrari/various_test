
import abc
import random


class AbstractPrototype(abc.ABC):
    """
    Interface that defines how the concrete prototypes should implement
    """

    @abc.abstractmethod
    def clone(self) -> 'AbstractPrototype':
        raise NotImplementedError


class A(AbstractPrototype):
    """
    Direct concrete prototype
    """

    def __init__(self) -> None:
        self.field1 = random.randint(1, 100 + 1)

    def clone(self) -> 'A':
        duplicate_a = A()
        duplicate_a.field1 = self.field1
        return duplicate_a


class B(A):
    """
    Subtype prototype
    """

    def __init__(self) -> None:
        super().__init__()
        self.field2 = random.randint(101, 200 + 1)

    def clone(self) -> 'B':
        """
        Notice how we have to take into consideration the superclasses fields
        """

        duplicate_b = B()
        duplicate_b.field1 = self.field1
        duplicate_b.field2 = self.field2
        return duplicate_b


if __name__ == "__main__":
    # main class clone
    a1 = A()
    print(f"a1 {id(a1)}: {a1.field1}")

    a2 = a1.clone()
    print(f"a2 {id(a2)}: {a2.field1}")

    # subclass clone
    b1 = B()
    print(f"b1 {id(b1)}: {b1.field1}, {b1.field2}")

    b2 = b1.clone()
    print(f"b2 {id(b2)}: {b2.field1}, {b2.field2}")
