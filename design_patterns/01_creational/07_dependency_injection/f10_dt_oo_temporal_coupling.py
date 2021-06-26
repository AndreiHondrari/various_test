"""
The problem with using "property"/setter injection is that it creates
temporal coupling forcing you to call one method after another in order
for some algorithm in a client method to work.
"""

from typing import Optional


class MissingDependencyException(Exception):
    pass


class Service:

    def use(self) -> None:
        print("Service is being used")


class Client:

    def __init__(self) -> None:
        self._dependency: Optional[Service] = None

    def initialize(self, service: Service) -> None:
        """
        Setter that injects our dependency service
        """

        self._dependency = service

    def do_something(self) -> None:
        """
        Client method that uses the dependency
        """

        # safeguard against a non-initialized dependency
        if self._dependency is None:
            raise MissingDependencyException

        # actual use of the dependency
        self._dependency.use()


if __name__ == '__main__':
    client = Client()

    print("# Use the client without initializing it with a dependency")
    try:
        client.do_something()
    except MissingDependencyException:
        print("MissingDependencyException was raised")

    print("\n# Initialize the dependency and then use the client")
    service = Service()
    client.initialize(service)
    client.do_something()
