import abc
from typing import Optional


class Handler(abc.ABC):

    def __init__(self, name: str) -> None:
        self._successor: Optional['Handler'] = None
        self.name = name

    @abc.abstractmethod
    def execute(self) -> None:
        raise NotImplementedError

    def handle_request(self) -> None:
        self.execute()

        if self._successor is not None:
            self._successor.handle_request()

    def add_successor(self, successor: 'Handler') -> 'Handler':
        self._successor = successor
        return successor


class HandlerOne(Handler):

    def execute(self) -> None:
        print(f"[handler one][{self.name}] does")


class HandlerTwo(Handler):

    def execute(self) -> None:
        print(f"[handler two][{self.name}] does")


class HandlerThree(Handler):

    def execute(self) -> None:
        print(f"[handler three][{self.name}] does")


class Client:

    def __init__(self, handler: Handler) -> None:
        self._handler = handler

    def run(self) -> None:
        self._handler.handle_request()


if __name__ == '__main__':

    handler1 = HandlerOne("Jeff")
    handler2 = handler1.add_successor(HandlerTwo("Luigi"))
    handler3 = handler2.add_successor(HandlerThree("Xavier"))
    handler3.add_successor(HandlerThree("Gunther"))

    client = Client(handler1)

    print("# Run client")
    client.run()
