import time
import random
from typing import Optional


class LatentDependency:

    def __init__(self, name: str) -> None:
        self.name = name
        print(f"Start heavy init for {self.name}...")
        latency = random.randint(1, 2)
        time.sleep(latency)  # simulating slow initialization
        print(f"Ended heavy init for {self.name}")

    def scream(self) -> None:
        print(f"{id(self)} ### I scream, u scream, {self.name} screams ! ###")


class NonLatentDependency:

    def provide_answer_to_everything(self) -> int:
        return 40 + 2


class Compound:

    def __init__(self) -> None:
        self._latent_dependency_1: Optional[LatentDependency] = None
        self._latent_dependency_2: Optional[LatentDependency] = None
        self._non_latent_dependency = NonLatentDependency()

    def _fetch_dependency_1(self) -> LatentDependency:
        # initialization segment
        if self._latent_dependency_1 is None:
            self._latent_dependency_1 = LatentDependency("JEFF")

        # retrieval segment
        return self._latent_dependency_1

    def _fetch_dependency_2(self) -> LatentDependency:
        # initialization segment
        if self._latent_dependency_2 is None:
            self._latent_dependency_2 = LatentDependency("ARNOLD")

        # retrieval segment
        return self._latent_dependency_2

    def do_simple(self) -> None:
        """Usage of a non-latent dependency"""
        answer = self._non_latent_dependency.provide_answer_to_everything()
        print(f"The Answer to everything is {answer}")

    def do_something(self) -> None:
        """Usage of latent dependencies"""
        dependency1: LatentDependency = self._fetch_dependency_1()
        dependency1.scream()

        dependency2: LatentDependency = self._fetch_dependency_2()
        dependency2.scream()


if __name__ == '__main__':
    our_compound = Compound()

    print("# Non-latent action")
    our_compound.do_simple()  # just stuff right away

    print("\n# First latent action")
    our_compound.do_something()  # takes a while to initialize the dependencies

    print("\n# Subsequent non-latent action (previously latent)")
    our_compound.do_something()  # on subsequent calls it just works faster
