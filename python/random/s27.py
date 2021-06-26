
from typing import Generic, TypeVar

T = TypeVar('T')


class X:
    def bla(self) -> None:
        print("bla")


class A(Generic[T], X):

    def do_some(self, a: T) -> None:
        print(a)


if __name__ == '__main__':
    a1 = A[int]()
    a1.do_some(10)
    a1.do_some("fwafa")
    a1.bla()
