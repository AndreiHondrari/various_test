import abc


class Implementor(abc.ABC):
    """
    Defines the operations that can be used by the abstraction
    """

    @abc.abstractmethod
    def do_this(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def do_that(self) -> None:
        raise NotImplementedError


class Abstraction(abc.ABC):
    """
    Provides an interface for the user code and depends on implementors
    to perform anything
    """

    def __init__(self, implementor: Implementor):
        self._implementor = implementor

    @abc.abstractmethod
    def do(self) -> None:
        raise NotImplementedError


class RefinedAbstraction(Abstraction, metaclass=abc.ABCMeta):
    """
    An extension to the original abstraction, doing more than it.
    This is just a sample of how the hierarchy of the abstraction can evolve
    independently from the implementors hierarchy.
    """

    @abc.abstractmethod
    def do_more(self) -> None:
        raise NotImplementedError


# concrete classes for Implementor, Abstraction and RefinedAbstraction
class Implementor1(Implementor):

    def do_this(self) -> None:
        print("[IMPL 1 ONE] doing this")

    def do_that(self) -> None:
        print("[IMPL 1 ONE] doing that")


class Implementor2(Implementor):

    def do_this(self) -> None:
        print("[IMPL 2 TWO] doing this")

    def do_that(self) -> None:
        print("[IMPL 2 TWO] doing that")


class Concrete(Abstraction):

    def do(self) -> None:
        print("[CONCRETE] doing")
        self._implementor.do_this()


class RefinedConcrete(RefinedAbstraction):

    def do(self) -> None:
        print("[REFINED CONCRETE] doing")
        self._implementor.do_this()

    def do_more(self) -> None:
        print("[REFINED CONCRETE] doing MORE")
        self._implementor.do_this()
        self._implementor.do_that()


if __name__ == '__main__':
    print("# Create implementors")
    impl1 = Implementor1()
    impl2 = Implementor2()

    print("# Create and use regular concrete gateway instances")

    print("\n# Concrete 1")
    concrete1 = Concrete(impl1)
    concrete1.do()

    print("\n# Concrete 2")
    concrete2 = Concrete(impl2)
    concrete2.do()

    print("\n# Refined Concrete 1")
    ref_concrete1 = RefinedConcrete(impl1)
    ref_concrete1.do()
    ref_concrete1.do_more()

    print("\n# Refined Concrete 2")
    ref_concrete2 = RefinedConcrete(impl2)
    ref_concrete1.do()
    ref_concrete2.do_more()
