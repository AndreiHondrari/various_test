

# define classes to be instantiated by the factory

class A:

    def __init__(self, created_by: str) -> None:
        self.created_by: str = created_by

    def __str__(self) -> str:
        return f"A({id(self)}) by {self.created_by}"


class B:

    def __init__(self, created_by: str) -> None:
        self.created_by: str = created_by

    def __str__(self) -> str:
        return f"A({id(self)}) by {self.created_by}"


# define the factory

class Factory:

    def __init__(self, name: str) -> None:
        self.name: str = name

    def make_a(self) -> A:
        return A(self.name)

    def make_b(self) -> B:
        return B(self.name)


# define the factory user

class FactoryUser:

    def __init__(self, factory: Factory) -> None:
        self.factory = factory

    def do_something(self) -> None:
        a: A = self.factory.make_a()
        b: B = self.factory.make_b()

        print(f"From factory user [A]: {str(a)}")
        print(f"From factory user [B]: {str(b)}")


if __name__ == "__main__":

    # simple factory usage
    print("Simple factory usage")
    x_factory = Factory("X-factory")
    a1: A = x_factory.make_a()
    b1: B = x_factory.make_b()
    print(f"Simple [A]: {str(a1)}")
    print(f"Simple [B]: {str(b1)}")

    # factory used by another object
    print("\nFactory from within another object")
    y_factory = Factory("Y-factory")
    factory_user = FactoryUser(y_factory)
    factory_user.do_something()
