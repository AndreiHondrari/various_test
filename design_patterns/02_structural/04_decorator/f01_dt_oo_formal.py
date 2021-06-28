import abc


class Component(abc.ABC):

    def __init__(self, name: str) -> None:
        self.name = name

    @abc.abstractmethod
    def do_something(self) -> None:
        raise NotImplementedError


class Decorator(Component, metaclass=abc.ABCMeta):

    def __init__(self, wrapee: Component, name: str) -> None:
        super().__init__(name)
        self._wrapee = wrapee

    def do_something(self) -> None:
        self._wrapee.do_something()


class ConcreteComponent1(Component):

    def do_something(self) -> None:
        print(f"Doing things the concrete {self.name} ONE way")


class ConcreteComponent2(Component):

    def do_something(self) -> None:
        print(f"Doing things the concrete {self.name} DIFFERENT way")


class ConcreteDecorator1(Decorator):

    def do_something(self) -> None:
        print(f"[DEC 1] Before {self._wrapee.name} in {self.name}")
        super().do_something()
        print(f"[DEC 1] After {self._wrapee.name} in {self.name}")


class ConcreteDecorator2(Decorator):

    def do_something(self) -> None:
        print(f"[DEC 2] Before {self._wrapee.name} in {self.name}")
        super().do_something()
        print(f"[DEC 2] After {self._wrapee.name} in {self.name}")


if __name__ == "__main__":

    print("# Define two concrete components")
    component1 = ConcreteComponent1("Jeff")
    component2 = ConcreteComponent2("Luigi")

    print("# Decorate each component with each decorator")
    decorated1 = ConcreteDecorator1(component1, "Romania")
    decorated2 = ConcreteDecorator2(component1, "Poland")
    decorated3 = ConcreteDecorator1(component2, "Norway")
    decorated4 = ConcreteDecorator2(component2, "Belgium")

    print("\n# Execute decorated 1")
    decorated1.do_something()

    print("\n# Execute decorated 2")
    decorated2.do_something()

    print("\n# Execute decorated 3")
    decorated3.do_something()

    print("\n# Execute decorated 4")
    decorated4.do_something()
