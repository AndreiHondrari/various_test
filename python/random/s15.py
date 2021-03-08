
import random as rd
from typing import Type


class X:
    pass


class A(X):
    pass


class B(X):
    pass


if __name__ == "__main__":
    bla: Type[X] = rd.choice([A, B])
