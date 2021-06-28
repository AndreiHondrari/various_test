import abc


class Target(abc.ABC):
    """
    The kind of interface the client wants
    """

    @abc.abstractmethod
    def do_something(self) -> None:
        raise NotImplementedError


class Client:
    """
    The class that uses a dependency, and can't directly use the adaptee
    """

    def __init__(self, target: Target):
        self._dependency_target = target

    def do(self) -> None:
        print("Client shoots at target")
        self._dependency_target.do_something()
        print("Client finalized")


class Adaptee:
    """
    The class that has the functionality that the client wants
    """

    def perform_something(self) -> None:
        """
        Functionality needed by the client.
        Named very specific within this class.
        """
        print("Adaptee functionality executing")


class Adapter(Target):
    """
    Implements the interface that the client expects while
    minding the gap to the adaptee
    """

    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    def do_something(self) -> None:
        print("Adapter closing the gap towards the adaptee")
        self._adaptee.perform_something()
        print("Adapter gap closed")


if __name__ == '__main__':
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client = Client(adapter)

    print("# Executing the client")
    client.do()
