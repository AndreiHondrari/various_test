import abc
from typing import Dict, Tuple, Generic, TypeVar, Type


class Flyweight(abc.ABC):

    @abc.abstractmethod
    def do_something(self, unique_state_a: int, unique_state_b: int) -> None:
        raise NotImplementedError


T = TypeVar('T', bound=Flyweight)


class FlyweightFactory(Generic[T]):

    def __init__(self) -> None:
        self._cached: Dict[Tuple[int, int], Flyweight] = dict()

    def obtain_flyweight(
        self,
        flyweight_subclass: Type[T],
        repeating_state_a: int,
        repeating_state_b: int,
    ) -> Flyweight:
        if (repeating_state_a, repeating_state_b) not in self._cached:
            self._cached[
                (repeating_state_a, repeating_state_b)
            ] = flyweight_subclass()

        return self._cached[(unique_state_a, unique_state_b)]


class ConcreteFlyweightX(Flyweight):

    def do_something(self, unique_state_a: int, unique_state_b: int) -> None:
        print
