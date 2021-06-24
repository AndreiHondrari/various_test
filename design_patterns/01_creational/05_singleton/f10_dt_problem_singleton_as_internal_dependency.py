"""
Now the problem with singletons is that if it is used directly in some
class, then you have no control over the instance that gets passed by it to
your custom class, and it forces you to succumb to ugly internal fiddling ->
that only makes your class a whitebox, and not a proper module.
"""

import abc
from typing import Type, Optional, Any


class AbstractFunctionality(abc.ABC):

    @abc.abstractmethod
    def do_something(self) -> None:
        raise NotImplementedError


class SomeSingleton(AbstractFunctionality):

    _instance: Optional['SomeSingleton'] = None

    @classmethod
    def get_instance(cls: Type['SomeSingleton']) -> 'SomeSingleton':
        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

    def do_something(self) -> None:
        print("I am a singleton !!")


class NotSingletonDependency(AbstractFunctionality):

    def __init__(self, name: str):
        self.name = name

    def do_something(self) -> None:
        print(f"I am {self.name}")


class UglyCustom:
    """
    A nasty class using singleton directly
    """

    def __init__(self) -> None:
        self._dependency: Any = SomeSingleton.get_instance()

    def use_dependency(self) -> None:
        self._dependency.do_something()


class BeautifulCustom:
    """
    A beautiful class using singleton as a passed dependency
    """

    def __init__(self, dependency: Any):
        self._dependency: Any = dependency

    def use_dependency(self) -> None:
        self._dependency.do_something()


if __name__ == "__main__":
    # see the ugly
    print("See the ugly")
    print("Step 1 - create")
    ugly_instance = UglyCustom()
    ugly_instance.use_dependency()

    # let's change that internal dependency in a nasty way, because
    # we can't pass it an instantiation time
    # we're lucky this is Python and it's dynamic, but if it were something
    # like C++ you would have a lot of fun right now ...
    print("Step 2 - ugly alteration")
    ugly_instance._dependency = NotSingletonDependency(
        "ugly injected dependency"
    )
    ugly_instance.use_dependency()

    # see the beautiful
    print("\nSee the beautiful")
    print("Nice instance #1")
    nice_dependency_1 = NotSingletonDependency("Jeff")
    nice_instance_1 = BeautifulCustom(nice_dependency_1)
    nice_instance_1.use_dependency()

    print("\nNice instance #2")
    nice_dependency_2 = NotSingletonDependency("Gordon Freeman")
    nice_instance_2 = BeautifulCustom(nice_dependency_2)
    nice_instance_2.use_dependency()
