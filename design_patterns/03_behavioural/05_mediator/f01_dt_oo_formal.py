import abc
from typing import Optional


class Component(abc.ABC):

    def __init__(self) -> None:
        self._mediator: Optional['Mediator'] = None

    def _notify_mediator(self) -> None:
        if self._mediator is not None:
            self._mediator.notify(self)

    def register_mediator(self, mediator: 'Mediator') -> None:
        self._mediator = mediator


class Mediator(abc.ABC):

    @abc.abstractmethod
    def notify(self, sender: Component) -> None:
        raise NotImplementedError


class ComponentA(Component):

    def event_foo(self) -> None:
        print("[CA] foo event")
        self._notify_mediator()

    def do_this(self) -> None:
        print("[CA] doing this")


class ComponentB(Component):

    def event_bar(self) -> None:
        print("[CB] bar event")
        self._notify_mediator()

    def do_that(self) -> None:
        print("[CB] doing that")


class ComponentC(Component):

    def event_baz(self) -> None:
        print("[CC] baz event")
        self._notify_mediator()

    def do_something_else(self) -> None:
        print("[CC] doing something else")


class ConcreteMediator(Mediator):

    def __init__(
        self,
        component_a: ComponentA,
        component_b: ComponentB,
        component_c: ComponentC,
    ) -> None:
        self._component_a = component_a
        self._component_b = component_b
        self._component_c = component_c

    def notify(self, sender: Component) -> None:

        if isinstance(sender, ComponentA):
            self._component_b.do_that()

        if isinstance(sender, ComponentB):
            self._component_c.do_something_else()

        if isinstance(sender, ComponentC):
            self._component_a.do_this()
            self._component_b.do_that()


if __name__ == '__main__':
    component_a = ComponentA()
    component_b = ComponentB()
    component_c = ComponentC()

    mediator = ConcreteMediator(
        component_a=component_a,
        component_b=component_b,
        component_c=component_c,
    )
    component_a.register_mediator(mediator)
    component_b.register_mediator(mediator)
    component_c.register_mediator(mediator)

    print("# Component A receives event")
    component_a.event_foo()

    print("\n# Component B receives event")
    component_b.event_bar()

    print("\n# Component C receives event")
    component_c.event_baz()
