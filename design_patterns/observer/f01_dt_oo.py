"""
Observer pattern - Object-oriented paradigm demonstration
"""
import random
import time

from abc import ABC, abstractmethod
from typing import Dict
from datetime import datetime


# Interfaces

class Observer(ABC):
    """
    Observer interface
    """

    @abstractmethod
    def update(self, subject):
        pass


class Subject(ABC):
    """
    Subject interface
    """

    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def unregister_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


# Mixins

class SubjectMixin(Subject):
    """
    Standard functionality for the subject
    """

    def __init__(self):
        self.observers = {}

    def register_observer(self, observer: Observer):
        self.observers[id(observer)] = observer

    def unregister_observer(self, observer: Observer):
        self.observers.pop(id(observer), None)

    def update_observer(self, observer):
        observer.update(self)

    def notify_observers(self):
        for observer_id, observer in self.observers.items():
            self.update_observer(observer)


# Example usage

class SpeedSensor(SubjectMixin, Subject):

    def __init__(self):
        super().__init__()
        self.value: int = 0
        self.acquisition_moment: datetime = datetime.now()

    def alter_speed(self, new_speed):
        self.value = new_speed
        self.acquisition_moment = datetime.now()
        self.notify_observers()


class MomentaryAcceleration(Observer):

    def __init__(self, sensor: SpeedSensor):
        self.speed_sensor = sensor
        self.value: float = 0.0
        self.last_speed_value: int = 0
        self.last_acquisition_moment: datetime = datetime.now()

    @property
    def acceleration_value(self):
        return self.value

    def update(self, subject: Subject):
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
        self.values_history: Dict[datetime] = {}

    def update(self, subject: Subject):
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
    for _ in range(20):
        time.sleep(0.1 + random.random())
        new_speed = random.randint(0, 50)

        # change a value in the subject
        print(f"speed: {new_speed}")
        sensor.alter_speed(new_speed)

        # see how the observers updated themselves as a result
        print(f"acceleration: {acceleration.value}")
        history_manifest = "".join(
            map(lambda t: f"    - {t[0]} |    {t[1]}\n", history.values_history.items())
        )
        print(f"history:\n{history_manifest}")
