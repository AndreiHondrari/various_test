

from typing import TypeVar, Generic, Type, Optional, Any

T = TypeVar('T')


class Descr(Generic[T]):

    def __init__(self, val: T) -> None:
        self.val: T = val

    def __get__(self, obj: 'A', owner: Optional[Type[Any]] = None) -> T:
        return self.val


class A:
    x = Descr[int](10)
    bla = Descr[str]("fwafaw")


a1 = A()

m: int = a1.bla

print(m)
