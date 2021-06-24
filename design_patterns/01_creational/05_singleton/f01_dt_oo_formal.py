

from typing import Optional, Type


class Singleton:
    """
    Our singleton class that creates only one instance.
    Notice that if you had instantiation arguments (args, kwargs), then
    every subsequent Singleton() call with different arguments would not be
    deterministic or make sense, since only the first instance is relevant.
    You would have to raise an exception for different instantiation
    parameters, or create different instance for
    each combination of parameters.
    """

    _instance: Optional['Singleton'] = None

    def __new__(cls: Type['Singleton']) -> 'Singleton':
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance


if __name__ == "__main__":
    o1: Singleton = Singleton()
    o2: Singleton = Singleton()
    o3: Singleton = Singleton()

    print(f"o1 id: {id(o1)}")
    print(f"o2 id: {id(o2)}")
    print(f"o3 id: {id(o3)}")
