"""
Decorator pattern - Functional programming paradigm demonstration
"""

from typing import Callable


def do_something() -> None:
    print("Something")


def do_something_else() -> None:
    print("Something else")


def do_changed_this_way(wrapee: Callable[[], None]) -> Callable[[], None]:

    def wrapped() -> None:
        print("Before in THIS way")
        wrapee()
        print("After in THIS way")

    return wrapped


def do_changed_that_way(wrapee: Callable[[], None]) -> Callable[[], None]:

    def wrapped() -> None:
        print("Before in THAT way")
        wrapee()
        print("After in THAT way")

    return wrapped


if __name__ == '__main__':
    print("# Decorate functions")
    decorated1 = do_changed_this_way(do_something)
    decorated2 = do_changed_this_way(do_something_else)
    decorated3 = do_changed_that_way(do_something)
    decorated4 = do_changed_that_way(do_something_else)

    print("\n# Call decorated 1")
    decorated1()

    print("\n# Call decorated 2")
    decorated2()

    print("\n# Call decorated 3")
    decorated3()

    print("\n# Call decorated 4")
    decorated4()
