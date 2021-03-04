
import abc


# define the classes to be created

class Something(abc.ABC):
    """
    Supertype of the objects to be returned by the factory method
    """

    def __init__(self, created_by: str) -> None:
        self.created_by: str = created_by

    def talk(self) -> None:
        class_name = self.__class__.__name__
        print(f"I'm {class_name}({id(self)}) created by `{self.created_by}`")


class A(Something):
    pass


class B(Something):
    pass


# define our creator classes

class BaseCreator(abc.ABC):
    """
    The abstract class that defines the factory method
    """

    def __init__(self, name: str) -> None:
        self.name: str = name

    @abc.abstractmethod
    def create_something(self) -> Something:
        """
        THE factory method abstract definition
        """

        raise NotImplementedError

    def do_something(self) -> None:
        something: Something = self.create_something()
        something.talk()


class X(BaseCreator):
    """
    Creator subclass that implements the first version of the factory method
    """

    def create_something(self) -> A:
        return A(self.name)


class Y(BaseCreator):
    """
    Creator subclass that implements the second version of the factory method
    """

    def create_something(self) -> B:
        return B(self.name)


if __name__ == "__main__":
    print("Creating with X")
    x_creator: X = X("X-creator")
    x_creator.do_something()

    print("\nCreating with Y")
    y_creator: Y = Y("Y-creator")
    y_creator.do_something()
