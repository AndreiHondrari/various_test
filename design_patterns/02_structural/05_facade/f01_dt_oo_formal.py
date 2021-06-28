

class Subsystem1Component:

    def __init__(self, name: str) -> None:
        self.name = name

    def do_this(self) -> None:
        print(f"[SYS1] {self.name} does THIS")


class Subsystem2Component:

    def __init__(self, name: str) -> None:
        self.name = name

    def do_that(self) -> None:
        print(f"[SYS2] {self.name} does THAT")


class Facade:

    def __init__(
        self,
        subsystem1_component: Subsystem1Component,
        subsystem2_component: Subsystem2Component,
    ):
        self._ss1_component = subsystem1_component
        self._ss2_component = subsystem2_component

    def do(self) -> None:
        print("[Facade] doing...")
        self._ss1_component.do_this()
        self._ss2_component.do_that()


if __name__ == '__main__':
    print("# Create components and facade")
    ss1_component = Subsystem1Component("Jeff")
    ss2_component = Subsystem2Component("Luigi")
    facade = Facade(ss1_component, ss2_component)

    print("\n# Use the facade")
    facade.do()
