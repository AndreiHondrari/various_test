import abc

from typing import Any, Optional, List


class Iterator(abc.ABC):

    @abc.abstractmethod
    def has_next(self) -> bool:
        raise NotImplementedError

    @abc.abstractmethod
    def next(self) -> Any:
        raise NotImplementedError


class Aggregate(abc.ABC):

    @abc.abstractmethod
    def get_iterator(self) -> Iterator:
        raise NotImplementedError


class ConcreteIterator(Iterator):

    def __init__(self, aggregate: 'ConcreteAggregate') -> None:
        self._aggregate = aggregate
        self._total_elements = len(self._aggregate._items)
        self._current_element: Optional[int] = (
            0 if self._total_elements > 0 else None
        )

    def has_next(self) -> bool:
        return (
            self._current_element is not None and
            (self._current_element + 1) < self._total_elements
        )

    def next(self) -> int:
        if self.has_next():
            self._current_element += 1  # type: ignore
            return self._aggregate._items[self._current_element]

        raise Exception("Iteration is over")


class ConcreteAggregate(Aggregate):

    def __init__(self, new_items: List[int]) -> None:
        self._items = new_items

    def get_iterator(self) -> ConcreteIterator:
        return ConcreteIterator(self)


class Client:

    def __init__(self, limit: int) -> None:
        self._aggregate = ConcreteAggregate(list(range(limit)))

    def do(self) -> None:
        iterator: Iterator = self._aggregate.get_iterator()

        while iterator.has_next():
            next_item: int = iterator.next()
            print(f"Item: {next_item}")


if __name__ == '__main__':
    client = Client(5)
    client.do()
