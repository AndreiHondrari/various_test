"""
Observer pattern - Object-oriented paradigm demonstration
"""
import abc

from typing import Dict, cast


# Interfaces

class Observer(abc.ABC):
    """
    Observer interface
    """

    @abc.abstractmethod
    def notify(self, subject: 'Subject') -> None:
        raise NotImplementedError


class Subject(abc.ABC):
    """
    Subject interface
    """

    @abc.abstractmethod
    def attach(self, observer: Observer) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def detach(self, observer: Observer) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def notify_observers(self) -> None:
        raise NotImplementedError


class ConcreteSubject(Subject):
    """
    Subject
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self.observers: Dict[int, Observer] = {}

    def attach(self, observer: Observer) -> None:
        self.observers[id(observer)] = observer

    def detach(self, observer: Observer) -> None:
        self.observers.pop(id(observer), None)

    def notify_observers(self) -> None:
        print(f"[CS] [{self.name}] notifies observers")
        for observer_id, observer in self.observers.items():
            observer.notify(self)

    def do(self) -> None:
        print(f"{self.name} is doing stuff")
        self.notify_observers()


class ConcreteObserver(Observer):

    def __init__(self, name: str):
        self.name = name

    def notify(self, subject: Subject) -> None:
        actual_subject: ConcreteSubject = cast(ConcreteSubject, subject)
        print(f"[CO] [{self.name}] observes {actual_subject.name}")


if __name__ == '__main__':

    print("# First subject")
    o1 = ConcreteObserver("Maxwell")
    o2 = ConcreteObserver("Planck")
    o3 = ConcreteObserver("Musa al-Khwarizmi (al-Gebra)")
    s1 = ConcreteSubject("Jeff")
    s1.attach(o1)
    s1.attach(o2)
    s1.attach(o3)
    s1.do()

    print("\n# Second subject")
    o3 = ConcreteObserver("Rejewski")
    o4 = ConcreteObserver("Rozycki")
    o5 = ConcreteObserver("Zygalski")
    s2 = ConcreteSubject("Enigma")
    s2.attach(o3)
    s2.attach(o4)
    s2.attach(o5)
    s2.do()
