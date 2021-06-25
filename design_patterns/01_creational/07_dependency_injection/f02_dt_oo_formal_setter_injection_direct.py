from typing import Optional


class Service:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Service({self.name})"

    def use(self) -> None:
        print(f"I {str(self)} am being used")


class Client:

    def __init__(self) -> None:
        self.dependency: Optional[Service] = None

    def set_dependency(self, service: Service) -> None:
        self.dependency = service

    def do_something(self) -> None:
        print(f"Start using {str(self.dependency)} from client")

        if self.dependency is not None:
            self.dependency.use()


if __name__ == '__main__':
    # This is the composition root
    service1 = Service("X 111")
    service2 = Service("F 222")

    client = Client()
    client.do_something()

    print("\n# Using service 1")
    client.set_dependency(service1)
    client.do_something()

    print("\n# Using service 2")
    client.set_dependency(service2)
    client.do_something()
