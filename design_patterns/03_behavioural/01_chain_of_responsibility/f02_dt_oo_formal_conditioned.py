import abc
import enum
from typing import Optional, List


@enum.unique
class Condition(enum.IntEnum):
    RUN = 1
    FLY = 2
    TELEPORT = 3


class Handler(abc.ABC):

    def __init__(self, name: str, conditions: List[Condition]) -> None:
        print(f"Creating {name} with {[c.name for c in conditions]}")
        self._successor: Optional['Handler'] = None
        self._conditions: List[Condition] = conditions
        self.name: str = name

    @abc.abstractmethod
    def do_specific(self) -> None:
        raise NotImplementedError

    def do(self, condition: Condition) -> None:

        if condition in self._conditions:
            print(f"{self.name} satisfies condition")
            self.do_specific()
        else:
            print(f"{self.name} does NOT satisfy condition")

        if self._successor is not None:
            self._successor.do(condition)

    def add_successor(self, successor: 'Handler') -> 'Handler':
        self._successor = successor
        return successor


class HandlerOne(Handler):

    def do_specific(self) -> None:
        print(f"[handler one][{self.name}] does")


class HandlerTwo(Handler):

    def do_specific(self) -> None:
        print(f"[handler two][{self.name}] does")


class HandlerThree(Handler):

    def do_specific(self) -> None:
        print(f"[handler three][{self.name}] does")


class Client:

    def __init__(self, handler: Handler) -> None:
        self._handler = handler

    def run(self) -> None:
        self._handler.do(Condition.TELEPORT)


if __name__ == '__main__':

    print("# Create handlers and client")
    handler1 = HandlerOne("Jeff", [Condition.RUN, Condition.TELEPORT])
    handler2 = handler1.add_successor(
        HandlerTwo("Luigi", [Condition.RUN, Condition.FLY])
    )
    handler3 = handler2.add_successor(
        HandlerThree("Xavier", [Condition.TELEPORT])
    )
    handler3.add_successor(
        HandlerThree("Gunther", [Condition.RUN])
    )

    client = Client(handler1)

    print("\n# Run client")
    client.run()
