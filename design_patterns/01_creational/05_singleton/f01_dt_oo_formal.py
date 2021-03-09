

from typing import Optional


class SomethingUnique:

    __instance: Optional['SomethingUnique'] = None

    def __new__(cls, name: str) -> 'SomethingUnique':
        if cls.__instance is None:
            cls.__instance = super(SomethingUnique, cls).__new__(cls)

        return cls.__instance

    def __init__(self, name: str):
        self.name = name


if __name__ == "__main__":
    o1 = SomethingUnique('AAA')
    o2 = SomethingUnique('BBB')
    o3 = SomethingUnique('CCC')

    print(f"o1: {id(o1)}: {o1.name}")
    print(f"o1: {id(o2)}: {o2.name}")
    print(f"o1: {id(o3)}: {o3.name}")
