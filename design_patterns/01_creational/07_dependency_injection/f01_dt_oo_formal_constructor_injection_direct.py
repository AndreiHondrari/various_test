

class Service:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Service({self.name})"

    def use(self) -> None:
        print(f"I {str(self)} am being used")


class Client:

    def __init__(self, service: Service, name: str):
        """
        Constructor that injects our dependency service
        """

        self.name = name
        self.dependency = service

    def __str__(self) -> str:
        return f"Client({self.name})"

    def do_something(self) -> None:
        """
        Client method that uses the dependency
        """

        print(f"Start using {str(self.dependency)} from {str(self)}")
        self.dependency.use()


if __name__ == '__main__':
    # This is the composition root

    print("# Using service 1")
    service1 = Service("X 111")
    client1 = Client(service1, "JEFF")
    client1.do_something()

    print("\n# Using service 2")
    service2 = Service("F 222")
    client2 = Client(service2, "ARNOLD")
    client2.do_something()
