
import abc


# declare family of objects to be created by the factories

# first inheritance tree
class A(abc.ABC):

    def __init__(self, created_by: str):
        self.created_by: str = created_by

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"I'm {class_name}({id(self)}) created by: {self.created_by}"


class AFamily1(A):
    pass


class AFamily2(A):
    pass


# second inheritance tree
class B(abc.ABC):

    def __init__(self, created_by: str):
        self.created_by: str = created_by

    def __str__(self) -> str:
        class_name = self.__class__.__name__
        return f"I'm {class_name}({id(self)}) created by: {self.created_by}"


class BFamily1(B):
    pass


class BFamily2(B):
    pass


"""
Notice how A and B subclasses don't share the same supertype but rather
they are related laterally from the inheritance tree
AFamily1 and BFamily1 are from the same family, the same way as
AFamily2 and BFamily2 is.
"""


# declare factories

class X(abc.ABC):
    """
    The abstract factory
    """

    def __init__(self, name: str):
        self.name: str = name

    @abc.abstractmethod
    def create_a(self) -> A:
        raise NotImplementedError

    @abc.abstractmethod
    def create_b(self) -> B:
        raise NotImplementedError


class Family1Factory(X):
    """
    First concrete factory for objects family #1
    """

    def create_a(self) -> AFamily1:
        return AFamily1(self.name)

    def create_b(self) -> BFamily1:
        return BFamily1(self.name)


class Family2Factory(X):
    """
    Second concrete factory for objects family #2
    """

    def create_a(self) -> AFamily2:
        return AFamily2(self.name)

    def create_b(self) -> BFamily2:
        return BFamily2(self.name)


if __name__ == "__main__":
    print("Family 1 of objects")
    y_factory = Family1Factory("Family-ONE-Factory")
    a1 = y_factory.create_a()
    b1 = y_factory.create_b()
    print(str(a1))
    print(str(b1))

    print("\nFamily 2 of objects")
    z_factory = Family2Factory("Family-TWO-Factory")
    a2 = z_factory.create_a()
    b2 = z_factory.create_b()
    print(str(a2))
    print(str(b2))
