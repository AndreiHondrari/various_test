from typing import Type, Dict


class Multiton:
    """
    Our singleton registry
    """

    _instances_map: Dict[str, 'Multiton'] = dict()

    @classmethod
    def lookup_instance(cls: Type['Multiton'], name: str) -> 'Multiton':
        if name in cls._instances_map:
            return cls._instances_map[name]

        cls._instances_map[name] = cls()
        return cls._instances_map[name]


class MultitonV2:
    """
    Second version of a multiton
    """

    _instances_map: Dict[str, 'MultitonV2'] = dict()

    def __new__(cls: Type['MultitonV2'], name: str) -> 'MultitonV2':
        if name in cls._instances_map:
            return cls._instances_map[name]

        cls._instances_map[name] = object.__new__(cls)
        return cls._instances_map[name]


if __name__ == '__main__':
    print("Simple multiton\n---------------")
    o1: Multiton = Multiton.lookup_instance('jeff')
    o2: Multiton = Multiton.lookup_instance('arnold')
    o3: Multiton = Multiton.lookup_instance('jeff')

    print(f"o1 id : {id(o1)}")
    print(f"o2 id : {id(o2)}")
    print(f"o3 id : {id(o3)}")

    print("\nMultiton v2\n---------------")
    o4: MultitonV2 = MultitonV2('jeff')
    o5: MultitonV2 = MultitonV2('arnold')
    o6: MultitonV2 = MultitonV2('jeff')

    print(f"o4 id : {id(o4)}")
    print(f"o5 id : {id(o5)}")
    print(f"o6 id : {id(o6)}")
