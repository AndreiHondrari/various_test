"""
Factory method pattern
"""

from abc import ABC, abstractmethod


# interfaces
class Operation(ABC):

    @abstractmethod
    def exec(self, a: int, b: int) -> int:
        raise NotImplementedError


class MathematicalOperation(ABC):

    @abstractmethod
    def get_operation(self) -> Operation:
        """
        This is the factory method that will be used in the subclass
        to return the instance that interests us
        """
        raise NotImplementedError

    def calculate(self, a: int, b: int) -> int:
        """
        Uses the factory method to generate an instance that has a specific
        interface (in this case, it has the exec method), and then it
        uses that interface of the instance.
        """
        operation_function = self.get_operation()  # creation
        return operation_function.exec(a, b)  # usage


# interface implementations for the types to be returned by the factory method
class Addition(Operation):

    def exec(self, a: int, b: int) -> int:
        return a + b


class Multiplication(Operation):

    def exec(self, a: int, b: int) -> int:
        return a * b


# subclasses of the creator class that has the factory method
class AdditionOperation(MathematicalOperation):

    def get_operation(self) -> Operation:
        return Addition()


class MultiplicationOperation(MathematicalOperation):

    def get_operation(self) -> Operation:
        return Multiplication()


if __name__ == "__main__":
    a = 11
    b = 22

    add_operation = AdditionOperation()
    add_result = add_operation.calculate(a, b)
    print(f"Addition operation: {a} + {b} = {add_result}")

    multiply_operation = MultiplicationOperation()
    multiply_result = multiply_operation.calculate(a, b)
    print(f"Multiplication operation: {a} x {b} = {multiply_result}")
