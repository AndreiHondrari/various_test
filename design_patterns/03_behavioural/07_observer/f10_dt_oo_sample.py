"""
Observer pattern - Object-oriented paradigm demonstration
"""
import random

from abc import ABC, abstractmethod
from typing import Dict
from datetime import datetime, timedelta


# Interfaces

class Observer(ABC):
    """
    Observer interface
    """

    @abstractmethod
    def update(self, subject: 'Subject') -> None:
        raise NotImplementedError


class Subject(ABC):
    """
    Subject interface
    """

    @abstractmethod
    def register_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def unregister_observer(self, observer: Observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notify_observers(self) -> None:
        raise NotImplementedError


# Mixins

class SubjectMixin(Subject):
    """
    Standard functionality for the subject
    """

    def __init__(self) -> None:
        self.observers: Dict[int, Observer] = {}

    def register_observer(self, observer: Observer) -> None:
        self.observers[id(observer)] = observer

    def unregister_observer(self, observer: Observer) -> None:
        self.observers.pop(id(observer), None)

    def notify_observers(self) -> None:
        for observer_id, observer in self.observers.items():
            observer.update(self)


# Example usage

class SpeedSensor(SubjectMixin, Subject):

    def __init__(self) -> None:
        super().__init__()
        self.value: int = 0
        self.acquisition_moment: datetime = datetime.now()

    def alter_speed(
        self,
        new_speed: int,
        acquisition_moment: datetime
    ) -> None:
        self.value = new_speed
        self.acquisition_moment = acquisition_moment
        self.notify_observers()


class MomentaryAcceleration(Observer):

    def __init__(self, sensor: SpeedSensor):
        self.speed_sensor = sensor
        self.value: float = 0.0
        self.last_speed_value: int = 0
        self.last_acquisition_moment: datetime = datetime.now()

    @property
    def acceleration_value(self) -> float:
        return self.value

    def update(self, subject: Subject) -> None:
        assert isinstance(subject, SpeedSensor)

        # determine the duration
        previous_moment = self.last_acquisition_moment
        current_moment = self.speed_sensor.acquisition_moment
        duration = (current_moment - previous_moment).total_seconds()

        if duration < 1.0:
            return  # do nothing

        # calculate the instant acceleration value
        self.value = (
            self.speed_sensor.value - self.last_speed_value
        ) / duration

        # backtrack
        self.last_speed_value = self.speed_sensor.value
        self.last_acquisition_moment = self.speed_sensor.acquisition_moment


class SpeedHistory(Observer):

    def __init__(self, sensor: SpeedSensor):
        self.speed_sensor = sensor
        self.last_acquisition_moment: datetime = datetime.now()
        self.values_history: Dict[datetime, float] = {}

    def update(self, subject: Subject) -> None:
        assert isinstance(subject, SpeedSensor)

        # determine the duration
        previous_moment = self.last_acquisition_moment
        current_moment = self.speed_sensor.acquisition_moment
        duration = (current_moment - previous_moment).total_seconds()

        if duration < 1.0:
            return  # do nothing

        self.values_history[current_moment] = self.speed_sensor.value
        self.last_acquisition_moment = self.speed_sensor.acquisition_moment


if __name__ == "__main__":
    # declare subject
    sensor = SpeedSensor()

    # declare observers
    acceleration = MomentaryAcceleration(sensor)
    history = SpeedHistory(sensor)

    # register observers
    sensor.register_observer(acceleration)
    sensor.register_observer(history)

    # example
    acquisition_moment = sensor.acquisition_moment  # first acquisition_moment

    for _ in range(20):
        new_speed = random.randint(0, 50)
        milliseconds_diff = (0.1 + random.random()) * 1000
        acquisition_moment = acquisition_moment + timedelta(
            milliseconds=milliseconds_diff
        )

        # change a value in the subject
        print(f"speed: {new_speed} at {acquisition_moment}")
        sensor.alter_speed(new_speed, acquisition_moment)

        # see how the observers updated themselves as a result
        print(f"acceleration: {acceleration.value}")
        history_manifest = "".join(
            map(
                lambda t: f"    - {t[0]} |    {t[1]}\n",
                history.values_history.items()
            )
        )
        print(f"history:\n{history_manifest}")
