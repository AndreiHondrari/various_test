from typing import List


class Memento:

    def __init__(self, state: int):
        self._state = state

    def get_state(self) -> int:
        return self._state


class Originator:

    def __init__(self) -> None:
        self._state = 0

    def set_state(self, state: int) -> None:
        self._state = state

    def get_state(self) -> int:
        return self._state

    def create_memento(self) -> Memento:
        return Memento(self._state)

    def restore_memento(self, memento: Memento) -> None:
        self._state = memento.get_state()

    def __str__(self) -> str:
        return f"Originator(state: {self._state})"


class Caretaker:

    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._steps: List[Memento] = []

    def go_forward(self) -> None:
        current_state_reminder = self._originator.create_memento()
        self._steps.append(current_state_reminder)
        current_state = self._originator.get_state()
        self._originator.set_state(current_state + 5)

    def go_backward(self) -> None:
        previous_state_reminder = self._steps.pop()
        self._originator.restore_memento(previous_state_reminder)


if __name__ == '__main__':
    originator = Originator()
    caretaker = Caretaker(originator)

    print("# Go forward three steps")
    caretaker.go_forward()
    caretaker.go_forward()
    caretaker.go_forward()
    print(str(originator))

    print("\n# Go back one steps")
    caretaker.go_backward()
    print(str(originator))
