"""
(Simple) Factory pattern
"""

import abc
import enum

from typing import List


# types to be constructed by the factory

@enum.unique
class DrugColor(enum.IntEnum):
    RED = enum.auto()
    BLUE = enum.auto()
    BLACK = enum.auto()


@enum.unique
class DrugEffect(enum.IntEnum):
    REVEALS_TRUTH = enum.auto()
    UNPLEASANT = enum.auto()
    PUKE_INDUCING = enum.auto()
    NUMBS_THE_MIND = enum.auto()
    PERIODIC_MEMORY_LOSS = enum.auto()
    RELAXING = enum.auto()
    HYPERACTIVITY = enum.auto()


class Drug(abc.ABC):

    @property
    def effects_str(self) -> str:
        return ", ".join(map(lambda effect: effect.name, self.effects))

    def __init__(
        self,
        color: DrugColor,
    ) -> None:
        self.color = color
        self.effects: List[DrugEffect] = []

    def add_effect(self, effect: DrugEffect) -> None:
        self.effects.append(effect)

    def remove_effect(self, effect: DrugEffect) -> None:
        self.effects.remove(effect)


class Capsule(Drug):
    pass


class Pill(Drug):
    pass


class Powder(Drug):
    pass


# the factory

@enum.unique
class DrugType(enum.IntEnum):
    PILL = enum.auto()
    CAPSULE = enum.auto()
    POWDER = enum.auto()


class DrugFactory:

    def __init__(self, color: DrugColor) -> None:
        self.color: DrugColor = color

    def make_drug(self, drug_type: DrugType) -> Drug:
        """
        This is what is encapsulated -> the creation logic
        """
        drug: Drug
        if (drug_type == DrugType.PILL):
            drug = Pill(self.color)
        elif (drug_type == DrugType.CAPSULE):
            drug = Capsule(self.color)
        elif (drug_type == DrugType.POWDER):
            drug = Powder(self.color)

        return drug


class DrugProvider:
    """
    Uses the factory
    """

    def __init__(
        self,
        red_drug_factory: DrugFactory,
        blue_drug_factory: DrugFactory,
        black_drug_factory: DrugFactory,
    ):
        """
        Usually the factory is part of another object that uses it
        to create a drug and perform some other operations on it
        """
        self._red_drugs_factory = red_drug_factory
        self._blue_drugs_factory = blue_drug_factory
        self._black_drugs_factory = black_drug_factory

    def create_red_relaxing_pill(self) -> Drug:
        red_pill = self._red_drugs_factory.make_drug(DrugType.PILL)
        red_pill.add_effect(DrugEffect.RELAXING)
        red_pill.add_effect(DrugEffect.PERIODIC_MEMORY_LOSS)
        return red_pill

    def create_red_truth_pill(self) -> Drug:
        red_pill = self._red_drugs_factory.make_drug(DrugType.PILL)
        red_pill.add_effect(DrugEffect.UNPLEASANT)
        red_pill.add_effect(DrugEffect.REVEALS_TRUTH)
        return red_pill

    def create_blue_amnesia(self) -> Drug:
        blue_pill = self._blue_drugs_factory.make_drug(DrugType.PILL)
        blue_pill.add_effect(DrugEffect.NUMBS_THE_MIND)
        blue_pill.add_effect(DrugEffect.PERIODIC_MEMORY_LOSS)
        return blue_pill

    def create_black_surprise(self) -> Drug:
        black_capsule = self._black_drugs_factory.make_drug(DrugType.CAPSULE)
        black_capsule.add_effect(DrugEffect.PUKE_INDUCING)
        black_capsule.add_effect(DrugEffect.NUMBS_THE_MIND)
        black_capsule.add_effect(DrugEffect.UNPLEASANT)
        return black_capsule

    def create_amfetamina(self) -> Drug:
        black_powder = self._black_drugs_factory.make_drug(DrugType.POWDER)
        black_powder.add_effect(DrugEffect.NUMBS_THE_MIND)
        black_powder.add_effect(DrugEffect.HYPERACTIVITY)
        return black_powder


if __name__ == "__main__":

    # factories
    red_factory = DrugFactory(DrugColor.RED)
    blue_factory = DrugFactory(DrugColor.BLUE)
    black_factory = DrugFactory(DrugColor.BLACK)

    # provider (factory user)
    drug_provider = DrugProvider(red_factory, blue_factory, black_factory)

    # blue pill
    blue_amensia = drug_provider.create_blue_amnesia()
    print(f"Blue effects: {str(blue_amensia.effects_str)}")

    # red pill
    red_truth = drug_provider.create_red_truth_pill()
    print(f"Red effects: {str(red_truth.effects_str)}")
