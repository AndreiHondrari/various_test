import abc
from typing import List, Union


class Component(abc.ABC):

    def __init__(self, name: str) -> None:
        self.name = name

    @abc.abstractmethod
    def do_something(self, command: str) -> None:
        raise NotImplementedError


class Compound(Component):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: List[Union[Component, Compound]] = list()

    def add_child(self, child: Union[Component, 'Compound']) -> None:
        self._children.append(child)

    def do_something(self, command: str) -> None:
        print(f"[Compound] [{self.name}] calls his children to do `{command}`")
        for child in self._children:
            child.do_something(command)


class ConcreteComponent1(Component):

    def do_something(self, command: str) -> None:
        print(f"[Concrete Component 1] [{self.name}] does `{command}`")


class ConcreteComponent2(Component):

    def do_something(self, command: str) -> None:
        print(
            f"[Concrete Component 2] [{self.name}] does `{command}` different"
        )


if __name__ == '__main__':
    print("# Define main compound")
    main_compound = Compound("Prometheus")

    print("# Define some standalone leafs")
    part1 = ConcreteComponent1("Xavier")
    part2 = ConcreteComponent1("Chuck")

    print("# Defining a compound and it's leafs")
    part3 = ConcreteComponent1("Jeff")
    part4 = ConcreteComponent1("Arnold")
    sub_compound = Compound("Shuttle")
    sub_compound.add_child(part3)
    sub_compound.add_child(part4)

    print("# Add everything to main")
    main_compound.add_child(part1)
    main_compound.add_child(part2)
    main_compound.add_child(sub_compound)

    print("\n# Use the tree to jump")
    main_compound.do_something("JUMP")

    print("\n# Use the tree to move left")
    main_compound.do_something("GO LEFT")
