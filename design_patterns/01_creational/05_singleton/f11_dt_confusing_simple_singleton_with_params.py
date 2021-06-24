"""
Notice that if you had instantiation arguments (args, kwargs), then
every subsequent Singleton() call with different arguments would not be
deterministic or make sense, since only one of the instantiation parameters
will be relevant.

In all programming languages, the actual instance will be always the first.
Depending on the language, the initialization parameters of either the first or
the last call will be in effect. In languages like C++, there is only one
method, the constructor, that will handle creation and initialization of
an instance, hence the memory and params of the first instantiation will be
permanent. In the case of Python, the creation and initialization are split
between __new__ and __init__. __new__ will return anything you want,
even a new instance of the class that you are working with or a random number,
if you really want it. __init__ will be called every time you instantiate, if
the instance returned by __new__ is of it's own type, otherwise it won't
call anything, hence if you call __new__ and return the same instance,
__init__ will be called for that instance every time, hence the last
initialization parameters will persist.

You would have to raise an exception for different instantiation
parameters, or create different instance for
each combination of parameters to counteract this inconsistent
instantiation behaviour.
"""

import abc
from typing import Type, Optional, Any


class Singleton:
    """
    Singleton with no initialization tracking.
    The last instantiation call will result in the last __init__ parameters
    to persist.
    """

    _instance: Optional['Singleton'] = None

    def __new__(
        cls: Type['Singleton'],
        *args: Any,
        **kwargs: Any
    ) -> 'Singleton':

        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self, name: str) -> None:
        self.name = name


class SingletonWithInitFlag:
    """
    Singleton with initialization tracking.
    The first initialization parameters are the only ones to persist.
    """

    _instance: Optional['SingletonWithInitFlag'] = None
    _is_initialized: bool = False

    def __new__(
        cls: Type['SingletonWithInitFlag'],
        *args: Any,
        **kwargs: Any
    ) -> 'SingletonWithInitFlag':

        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self, name: str) -> None:
        if SingletonWithInitFlag._is_initialized:
            return

        self.name = name
        SingletonWithInitFlag._is_initialized = True


if __name__ == "__main__":
    print("Simple singleton\n----------------")
    o1: Singleton = Singleton("Jeff")
    o2: Singleton = Singleton("Arnold")
    o3: Singleton = Singleton("Timothy")

    # notice the all of the following are Timothy, and Arnold and Jeff
    # are forgotten
    print(f"o1 id and name: {id(o1)} {o1.name}")
    print(f"o2 id and name: {id(o2)} {o2.name}")
    print(f"o3 id and name: {id(o3)} {o3.name}")

    print("\nSingletonWithInitFlag\n---------------------")
    o4: SingletonWithInitFlag = SingletonWithInitFlag("Jane")
    o5: SingletonWithInitFlag = SingletonWithInitFlag("Tiffany")
    o6: SingletonWithInitFlag = SingletonWithInitFlag("Esmeralda")

    # notice the all of the following are Jane
    print(f"o4 id and name: {id(o4)} {o4.name}")
    print(f"o5 id and name: {id(o5)} {o5.name}")
    print(f"o6 id and name: {id(o6)} {o6.name}")
