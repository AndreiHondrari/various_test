

class Service:

    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"Service({self.name})"

    def use(self) -> None:
        print(f"I {str(self)} am being used")


class Client:

    def __init__(self, default_service: Service) -> None:
        """
        Injecting a default service for.
        """

        self.dependency: Service = default_service

    def set_dependency(self, service: Service) -> None:
        """
        Setter that injects our dependency service
        """

        self.dependency = service

    def do_something(self) -> None:
        """
        Client method that uses the dependency
        """

        print(f"Start using {str(self.dependency)} from client")
        self.dependency.use()


if __name__ == '__main__':
    # This is the composition root
    default_service = Service("LOCAL")
    new_service = Service("NOUVEAU")

    client = Client(default_service)

    print("\n# Using default service")
    client.do_something()

    print("\n# Using new service")
    client.set_dependency(new_service)
    client.do_something()
