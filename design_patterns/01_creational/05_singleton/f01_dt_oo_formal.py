

from typing import Optional


class SingletonAlreadyInstantiatedError(Exception):
    pass


class SomethingUnique:
    """
    The singleton class.
    Overrides __new__ by creating only one instance per class.
    Raises an exception in the case of additional instantiation.
    """

    __instance: Optional['SomethingUnique'] = None

    @classmethod
    def get_instance(cls) -> Optional['SomethingUnique']:
        return cls.__instance

    def __new__(cls, name: str) -> 'SomethingUnique':
        if cls.__instance is not None:
            raise SingletonAlreadyInstantiatedError

        instance: 'SomethingUnique' = super(SomethingUnique, cls).__new__(cls)
        cls.__instance = instance
        return instance

    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    # first instantiation
    o1 = SomethingUnique('AAA')
    print(f"o1: {id(o1)}: {o1.name}")

    # subsequent instantiations
    try:
        o2 = SomethingUnique('BBB')
    except SingletonAlreadyInstantiatedError:
        print("o2 exception detected")
        pass

    try:
        o3 = SomethingUnique('CCC')
    except SingletonAlreadyInstantiatedError:
        print("o3 exception detected")
        pass

    # get the already existing instance
    o4: Optional[SomethingUnique] = SomethingUnique.get_instance()
    if o4 is not None:
        print(f"o4: {id(o4)}: {o4.name}")
    else:
        raise Exception("o4 shouldn't be none!")
