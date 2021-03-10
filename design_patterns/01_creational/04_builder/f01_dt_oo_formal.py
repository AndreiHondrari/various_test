
import abc
import random
import itertools
import functools

from typing import Set, Callable, Type, Any, List


# declare classes to be used

class Component(abc.ABC):

    @abc.abstractmethod
    def talk(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_operation(self) -> Callable[[int, int], int]:
        raise NotImplementedError

    @abc.abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError

    def __init__(self, number: int):
        self.number: int = number

    def calculate(self, other_value: int) -> int:
        operation = self.get_operation()
        self.number = operation(self.number, other_value)
        return self.number


class Component1(Component):

    def __str__(self) -> str:
        return f"C1({self.number})"

    def talk(self) -> None:
        print(f"I hereby declare: {self.number}")

    def get_operation(self) -> Callable[[int, int], int]:
        return lambda a, b: a + b


class Component2(Component):

    def __str__(self) -> str:
        return f"C2({self.number})"

    def talk(self) -> None:
        print(f"Here ye' have it: {self.number}")

    def get_operation(self) -> Callable[[int, int], int]:
        return lambda a, b: a * b


class Product:

    def __init__(self) -> None:
        self.components: Set[Component] = set()

    def __str__(self) -> str:
        components_str: str = ", ".join([
            str(c) for c in self.components
        ])
        return f"{id(self)}: {components_str}"

    def add_component(self, component: Component) -> None:
        self.components.add(component)

    def clear(self) -> None:
        self.components = set()


# declare the builder

class AbstractProductBuilder(abc.ABC):
    """
    The builder
    """

    @abc.abstractmethod
    def reset(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_result(self) -> Product:
        raise NotImplementedError

    @abc.abstractmethod
    def build_step_1(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def build_step_2(self) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def build_step_3(self) -> None:
        raise NotImplementedError


class ProductBuilderA(AbstractProductBuilder):

    def __init__(self) -> None:
        self.result = Product()

    def reset(self) -> None:
        self.result = Product()

    def get_result(self) -> Product:
        return self.result

    def build_step_1(self) -> None:
        """
        Adds a random component with random value
        """
        random_component_class: Type[Any] = random.choice([
            Component1,
            Component2,
        ])

        self.result.add_component(
            random_component_class(random.randint(1, 100 + 1))
        )

    def build_step_2(self) -> None:
        """
        Apply operation to itself with 2
        """

        SECOND_OPERAND = 2

        for component in self.result.components:
            component.calculate(SECOND_OPERAND)

    def build_step_3(self) -> None:
        """
        Post process by nullifying values over 100.
        """

        for component in self.result.components:
            if component.number > 100:
                component.number = 0


class ProductBuilderB(AbstractProductBuilder):

    def __init__(
        self,
        component_class: Type[Component],
        reduce_function: Callable[[int, int], int],
    ) -> None:
        self.result = Product()
        self.counter = itertools.count(5, 5)
        self.component_class: Type[Component] = component_class
        self.reduce_function: Callable[[int, int], int] = reduce_function

    def reset(self) -> None:
        self.result = Product()

    def get_result(self) -> Product:
        return self.result

    def build_step_1(self) -> None:
        """
        Add new specific component
        """
        new_component: Component = self.component_class(next(self.counter))
        self.result.add_component(new_component)

    def build_step_2(self) -> None:
        """
        For every component create a new component with the result of the
        calculation with 3 scaled with 100.

        ATTENTION: It doubles the number of components every time
        """

        SECOND_OPERAND = 3
        SCALE_VALUE = 100

        new_components: List[Component] = []

        for component in self.result.components:
            calculation_result = component.calculate(SECOND_OPERAND)
            new_components.append(
                self.component_class(calculation_result * SCALE_VALUE)
            )

        for new_component in new_components:
            self.result.add_component(new_component)

    def build_step_3(self) -> None:
        """
        Post process by reducing
        """

        reduced_value: int = 0
        if len(self.result.components) > 0:
            values: List[int] = [
                component.number for component in self.result.components
            ]
            reduced_value = functools.reduce(
                self.reduce_function,
                values
            )

        new_component: Component = self.component_class(reduced_value)
        self.result.clear()
        self.result.add_component(new_component)


class Director:
    """
    User of the builder objects
    """

    def __init__(self) -> None:
        self.builder = ProductBuilderA()
        self.products: List[Product] = []

    def switch_to_category_1(self) -> None:
        self.products = []

        for i in range(3):
            self.builder.reset()

            self.builder.build_step_1()
            self.builder.build_step_1()
            self.builder.build_step_1()
            self.builder.build_step_1()

            self.builder.build_step_3()
            self.products.append(self.builder.get_result())

    def switch_to_category_2(self) -> None:
        self.products = []

        for i in range(2):
            self.builder.reset()

            for j in range(random.randint(5, 10)):
                self.builder.build_step_1()

            self.builder.build_step_2()
            self.builder.build_step_3()
            self.products.append(self.builder.get_result())


if __name__ == "__main__":
    # builders
    builder_a = ProductBuilderA()
    builder_b = ProductBuilderB(Component1, lambda x, y: x // 2 + y // 2)
    builder_c = ProductBuilderB(Component2, lambda x, y: x // 10 * y // 10)

    print("BUILDER A\n---------\n")

    builder_a.build_step_1()
    builder_a.build_step_1()
    builder_a.build_step_1()
    product: Product = builder_a.get_result()
    print(f"Usage #1 {product}")

    builder_a.build_step_2()
    product = builder_a.get_result()
    print(f"Usage #2 {product}")

    builder_a.build_step_3()
    product = builder_a.get_result()
    print(f"Usage #3 {product}")

    print("\nBUILDER B\n---------\n")

    builder_b.build_step_1()
    builder_b.build_step_1()
    builder_b.build_step_1()
    builder_b.build_step_1()
    product = builder_b.get_result()
    print(f"Usage #1 {product}")

    builder_b.build_step_2()
    product = builder_b.get_result()
    print(f"Usage #2 {product}")

    builder_b.build_step_3()
    product = builder_b.get_result()
    print(f"Usage #3 {product}")

    print("\nBUILDER C\n---------\n")

    builder_c.build_step_1()
    builder_c.build_step_1()
    product = builder_c.get_result()
    print(f"Usage #1 {product}")

    builder_c.build_step_2()
    product = builder_c.get_result()
    print(f"Usage #2 {product}")

    builder_c.build_step_3()
    product = builder_c.get_result()
    print(f"Usage #3 {product}")

    print("\nDIRECTOR\n----------\n")

    director = Director()

    director.switch_to_category_1()
    d_products = list(map(str, director.products))
    print(f"Usage #1 {d_products}")

    director.switch_to_category_2()
    d_products = list(map(str, director.products))
    print(f"Usage #2 {d_products}")
