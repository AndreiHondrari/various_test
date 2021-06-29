import abc

# from typing import


class Command(abc.ABC):

    def __init__(self, name: str) -> None:
        self.name = name

    @abc.abstractmethod
    def execute(self) -> None:
        raise NotImplementedError


class Invoker:

    def __init__(
        self,
        action1: Command,
        action2: Command,
    ):
        self._action1: Command = action1
        self._action2: Command = action2

    def do_this(self) -> None:
        self._action1.execute()

    def do_that(self) -> None:
        self._action2.execute()


class ReceiverA:

    def __init__(self, name: str) -> None:
        self.name = name

    def foo(self) -> None:
        print(f"{self.name} casts")


class ReceiverB:

    def __init__(self, name: str) -> None:
        self.name = name

    def bar(self) -> None:
        print(f"{self.name} performs")


class ConcreteCommand1(Command):

    def __init__(self, name: str, receiver: ReceiverA):
        super().__init__(name)
        self._receiver = receiver

    def execute(self) -> None:
        print(f"[CC1] [{self.name}] passed to receiver {self._receiver.name}")
        self._receiver.foo()


class ConcreteCommand2(Command):

    def __init__(self, name: str, receiver: ReceiverB):
        super().__init__(name)
        self._receiver = receiver

    def execute(self) -> None:
        print(f"[CC2] [{self.name}] passed to receiver {self._receiver.name}")
        self._receiver.bar()


class ConcreteCommand3(Command):

    def __init__(
        self,
        name: str,
        receiver_1: ReceiverA,
        receiver_2: ReceiverB
    ):
        super().__init__(name)
        self._receiver_1 = receiver_1
        self._receiver_2 = receiver_2

    def execute(self) -> None:
        print(
            f"[CC3] [{self.name}] passed to receivers "
            f"{self._receiver_1.name} and {self._receiver_2.name}"
        )
        self._receiver_1.foo()
        self._receiver_2.bar()


class Client:

    def __init__(self) -> None:

        receiver_1 = ReceiverA("Jeff")
        command_1 = ConcreteCommand1("Alohomora", receiver_1)

        receiver_2 = ReceiverB("Ron Weasley")
        command_2 = ConcreteCommand2("Wingardium Leviosaa", receiver_2)

        self._invoker = Invoker(command_1, command_2)

    def run(self) -> None:
        self._invoker.do_this()
        self._invoker.do_that()


class Client2:

    def __init__(self) -> None:

        receiver_1 = ReceiverA("Severus")
        command_1 = ConcreteCommand1("Lacarnum Inflamari", receiver_1)

        receiver_2 = ReceiverA("Lucius")
        receiver_3 = ReceiverB("Voldemort")
        command_2 = ConcreteCommand3("Abracadabra", receiver_2, receiver_3)

        self._invoker = Invoker(command_1, command_2)

    def run(self) -> None:
        self._invoker.do_this()
        self._invoker.do_that()


if __name__ == '__main__':

    print("# Client 1 execution")
    client1 = Client()
    client1.run()

    print("\n# Client 2 execution")
    client2 = Client2()
    client2.run()
