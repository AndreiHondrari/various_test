
from abc import ABC, abstractmethod


def something(fun):
    def wrapper(self):
        print("Before fun")
        fun(self)
        print("After fun")

    return wrapper


class Base:

    @abstractmethod
    @something
    def some(self):
        pass


class Child(Base):

    # @something
    def some(self):
        print("Something something")


if __name__ == "__main__":
    c1 = Child()
    c1.some()
