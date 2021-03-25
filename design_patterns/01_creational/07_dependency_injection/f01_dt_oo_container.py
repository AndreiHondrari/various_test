
import abc
from typing import Optional, Type, Any, Generic, TypeVar

T = TypeVar('T')


# define services
class Service(abc.ABC):
    pass


class ServiceType1(Service, metaclass=abc.ABCMeta):
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


class ServiceType2(Service, metaclass=abc.ABCMeta):
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


class ClientServiceSetterInterface(abc.ABC):

    @abc.abstractmethod
    def set_service(self, service: Service) -> None:
        raise NotImplementedError


# class BaseServiceDescriptor:

class ServiceDescriptor(Generic[T]):

    def __init__(self, service_attribute: str) -> None:
        self._service_attribute: str = service_attribute

    def __get__(
        self,
        obj: 'Client',
        owner: Optional[Type[Any]] = None
    ) -> T:
        service: Optional[T] = (
            getattr(
                obj, self._service_attribute
            )
        )

        if service is None:
            raise ServiceNotAvailableError

        return service


class Client(ClientServiceSetterInterface):

    first_service = ServiceDescriptor[ServiceType1]("_first_service")
    second_service = ServiceDescriptor[ServiceType1]("_second_service")
    third_service = ServiceDescriptor[ServiceType2]("_third_service")
    fourth_service = ServiceDescriptor[ServiceType2]("_fourth_service")

    def __init__(self) -> None:
        self._first_service: Optional[ServiceType1] = None
        self._second_service: Optional[ServiceType1] = None
        self._third_service: Optional[ServiceType2] = None
        self._fourth_service: Optional[ServiceType2] = None

    def set_first_type_services(
        self,
        first_service: ServiceType1,
        second_service: ServiceType1,
    ) -> None:
        self._first_service = first_service
        self._second_service = second_service

    def set_second_type_services(
        self,
        third_service: ServiceType2,
        fourth_service: ServiceType2,
    ) -> None:
        self._third_service = third_service
        self._fourth_service = fourth_service

    def bark(self) -> None:
        self.first_service.do_something()
        self.third_service.do_something_else()
        self.second_service.do_something()
        self.fourth_service.do_something_else()


if __name__ == "__main__":
    pass
    # fst_service = ServiceX()
    # snd_service = ServiceY()
    # trd_service = ServiceF()
    # frt_service = ServiceG()
    #
    # client_d = Client()
    # client_d.woof()
