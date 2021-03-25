
import abc
from typing import Optional


# define services
class Service(abc.ABC):
    """
    A type of service to be injected
    """

    @abc.abstractmethod
    def do_something(self) -> None:
        raise NotImplementedError


class ServiceX(Service):

    def do_something(self) -> None:
        print(f"SX {id(self)} ..does")


class ServiceY(Service):

    def do_something(self) -> None:
        print(f"SY {id(self)} ..talks")


class ServiceType2(abc.ABC):
    """
    Another type of service to be injected
    """

    def do_something_else(self) -> None:
        raise NotImplementedError


class ServiceF(ServiceType2):

    def do_something_else(self) -> None:
        print(f"SF {id(self)} ..foo")


class ServiceG(ServiceType2):

    def do_something_else(self) -> None:
        print(f"SG {id(self)} ..bar")


# define client

class ServiceNotAvailableError(Exception):
    pass


class ClientA:
    """
    Constructor dependency injection
    """

    def __init__(self, service: Service):
        self.service: Service = service

    def bark(self) -> None:
        self.service.do_something()


class ClientB:
    """
    Setter dependency injection
    """

    def __init__(self) -> None:
        self.service: Optional[Service] = None

    def set_service(self, service: Service) -> None:
        self.service = service

    def bark(self) -> None:
        if self.service is None:
            raise ServiceNotAvailableError

        self.service.do_something()


class ClientCServiceSetterInterface(abc.ABC):
    """
    Interface for interface dependency injection.
    Enforces the setter that injects the service
    """

    @abc.abstractmethod
    def set_service(self, service: Service) -> None:
        raise NotImplementedError


class ClientC(ClientCServiceSetterInterface):
    """
    Interface dependency injection
    """

    def __init__(self) -> None:
        self.service: Optional[Service] = None

    def set_service(self, service: Service) -> None:
        self.service = service

    def bark(self) -> None:
        if self.service is None:
            raise ServiceNotAvailableError

        self.service.do_something()


class ClientD:
    """
    A client with multiple dependencies to be injected.
    Demonstrates how tedious it can be to inject dependencies from outside
    if the number of services is greater.
    """

    def __init__(
        self,
        first_service: Service,
        second_service: Service,
        third_service: ServiceType2,
        fourth_service: ServiceType2,
    ) -> None:
        self.first_service = first_service
        self.second_service = second_service
        self.third_service = third_service
        self.fourth_service = fourth_service

    def woof(self) -> None:
        self.first_service.do_something()
        self.third_service.do_something_else()
        self.second_service.do_something()
        self.fourth_service.do_something_else()


if __name__ == "__main__":
    # create client A
    print("Client A")
    service_for_a = ServiceX()
    client_a = ClientA(service_for_a)
    client_a.bark()

    # create client B
    print("\nClient B")
    service_for_b = ServiceX()
    client_b = ClientB()
    client_b.set_service(service_for_b)
    client_b.bark()

    # create client C
    print("\nClient C")
    service_for_c = ServiceY()
    client_c = ClientC()
    client_c.set_service(service_for_c)
    client_c.bark()

    # create client D
    print("\nClient D")
    fst_service = ServiceX()
    snd_service = ServiceY()
    trd_service = ServiceF()
    frt_service = ServiceG()

    client_d = ClientD(
        fst_service,
        snd_service,
        trd_service,
        frt_service,
    )
    client_d.woof()
