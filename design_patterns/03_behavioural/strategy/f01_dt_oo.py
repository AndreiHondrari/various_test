"""
Strategy pattern - Object-oriented paradigm demonstration
"""

import abc

from collections import namedtuple


TransitResult = namedtuple('TransitResult', ['logs', 'remaining_fuel'])


class TransitBehaviour(abc.ABC):
    """
    Strategy Interface
    """

    @abc.abstractmethod
    def transit(self, fuel_quantity: int, distance: int) -> TransitResult:
        raise NotImplementedError


class Fly(TransitBehaviour):
    """
    Strategy - for flight
    """

    def transit(self, fuel_quantity: int, distance: int) -> TransitResult:
        assert fuel_quantity >= 0
        assert distance > 0, "Distance must be positive"

        FUEL_CONSUMPTION_RATE = 1200

        logs = []

        # initial
        if fuel_quantity == 0:
            logs.append("Never takes off")
            return TransitResult(logs=logs, remaining_fuel=0)

        logs.append("Take-off")

        # fly
        transit_distance = (fuel_quantity // FUEL_CONSUMPTION_RATE) * 100
        logs.append(f"Fly for {transit_distance}km")

        # crash or land
        necessary_fuel = (distance // 100) * FUEL_CONSUMPTION_RATE
        if necessary_fuel > fuel_quantity:
            logs.append("Crash")
            remaining_fuel = 0
        else:
            logs.append("Land")
            remaining_fuel = fuel_quantity - necessary_fuel

        return TransitResult(
            logs=logs,
            remaining_fuel=remaining_fuel
        )


class Sail(TransitBehaviour):
    """
    Strategy - for sailing
    """

    def transit(self, fuel_quantity: int, distance: int) -> TransitResult:
        FUEL_CONSUMPTION_RATE = 10000
        logs = []

        # initial
        if fuel_quantity == 0:
            logs.append("Does not raise anchor")
            return TransitResult(logs=logs, remaining_fuel=0)

        logs.append("Raise anchor and start sailing")

        # sail
        transit_distance = (fuel_quantity // FUEL_CONSUMPTION_RATE) * 100
        logs.append(f"Cross the sea for {transit_distance}km")

        # halt
        logs.append("Drop anchor")

        necessary_fuel = (distance // 100) * FUEL_CONSUMPTION_RATE
        remaining_fuel = fuel_quantity - necessary_fuel
        return TransitResult(
            logs=logs,
            remaining_fuel=remaining_fuel if remaining_fuel >= 0 else 0
        )


class Station(TransitBehaviour):
    """
    Strategy - for doing nothing
    """

    def transit(self, fuel_quantity: int, distance: int) -> TransitResult:
        return TransitResult(
            logs=["Engine makes a weird noise and stops"],
            remaining_fuel=fuel_quantity
        )


class Vehicle(abc.ABC):
    """Context"""

    def __init__(
        self,
        name: str,
        fuel_quantity: int,
        transit_behaviour: TransitBehaviour
    ) -> None:
        self.name = name

        self._initial_fuel_quantity = fuel_quantity
        self.fuel_quantity = fuel_quantity

        # we attach the strategy to our context
        self.transit_behaviour = transit_behaviour

    def transit(self, distance: int) -> None:
        assert distance > 0

        # we use the strategy
        transit_result = self.transit_behaviour.transit(
            self.fuel_quantity,
            distance
        )

        # get the results of the strategy

        # state change in the context
        self.fuel_quantity = transit_result.remaining_fuel

        # compose description
        logs = list(map(lambda log: f"    - {log}\n", transit_result.logs))
        logs.append(f"    Remaining fuel: {self.fuel_quantity}\n")
        logs_manifest = "".join(logs)

        print(
            f"{self.name} transit outcome: \n"
            f"{logs_manifest}"
        )


if __name__ == "__main__":
    fly_behaviour = Fly()
    sail_behaviour = Sail()
    station_behaviour = Station()

    plane = Vehicle("XR-100", 1300, fly_behaviour)

    print("Plane transit #1")
    plane.transit(100)

    print("Plane transit #2")
    plane.transit(200)

    print("Plane transit #3")
    plane.transit(1)

    boat = Vehicle("Black Pearl", 11000, sail_behaviour)

    print("Black pearl sail #1")
    boat.transit(100)

    print("Black pearl sail #2")
    boat.transit(120)

    print("Black pearl sail #3")
    boat.transit(1)

    old_car = Vehicle("Lada", 20, station_behaviour)

    print("Old car transit #1")
    old_car.transit(1)

    print("Old car transit #2")
    old_car.transit(1)
