
import abc


# define services
class Service(abc.ABC):
    """
    Service Interface
    """

    @abc.abstractmethod
    def do_something(self) -> None:
        raise NotImplementedError


class ConcreteService(Service):
    """
    Concrete implementation of a service
    """

    def do_something(self) -> None:
        print(f"SX {id(self)} ..does")


# define client

class Client:
    """
    Constructor dependency injection
    """

    def __init__(self, service: Service):
        self.service: Service = service

    def use_service(self) -> None:
        self.service.do_something()


if __name__ == "__main__":
    """
    This is the composition root.
    """
    # perform constructor dependency injection
    concrete_service = ConcreteService()
    client = Client(concrete_service)
    client.use_service()
