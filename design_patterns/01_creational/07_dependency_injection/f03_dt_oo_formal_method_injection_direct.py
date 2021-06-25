

class Service:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Service({self.name})"

    def use(self) -> None:
        print(f"I {str(self)} am being used")


class Client:

    def do_something(self, service: Service) -> None:
        print(f"Start using {str(service)} from client")
        service.use()


if __name__ == '__main__':
    # This is the composition root
    service1 = Service("X 111")
    service2 = Service("F 222")

    client = Client()

    print("\n# Using service 1")
    client.do_something(service1)

    print("\n# Using service 2")
    client.do_something(service2)
