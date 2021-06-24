from typing import Type, Any, Dict


class Multiton:
    """
    Advanced version of multiton with type registration and parameters passing.
    """

    _instances_map: Dict[Type[Any], Any] = dict()

    def __new__(
        cls: Type['Multiton'],
        *args: Any,
        **kwargs: Any
    ) -> Any:
        if cls in Multiton._instances_map:
            return cls._instances_map[cls]

        cls._instances_map[cls] = object.__new__(cls)
        return cls._instances_map[cls]


class FirstSingletonType(Multiton):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(f"FirstSingletonType.__init__ args {args} kwargs {kwargs}")


class SecondSingletonType(Multiton):

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        print(f"SecondSingletonType.__init__ args {args} kwargs {kwargs}")


if __name__ == '__main__':
    # Notice how in both cases the instance is the same
    # for subsequent instantiation.
    # Notice that multitone, same as singletons have the
    # subsequent initialization problem in Python.
    print("FirstSingletonType\n------------------")
    f1: FirstSingletonType = FirstSingletonType(111)
    f2: FirstSingletonType = FirstSingletonType(222)
    print(f"f1 {id(f1)} | f2 {id(f2)}")

    print("\nSecondSingletonType\n-------------------")
    s1: SecondSingletonType = SecondSingletonType(333)
    s2: SecondSingletonType = SecondSingletonType(444)
    print(f"s1 {id(s1)} | s2 {id(s2)}")
