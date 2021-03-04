
import abc
import enum

from typing import Set, Union
from dataclasses import dataclass

"""
Age of Empires units factories

Context
-------
- knight: horse mounted military units. Good for close combat
- trebuchet: large catapult that has to be transported in a packed form.
  Good for distance siege attack
"""


# the game units

@dataclass
class UnitCoordinates:
    x: int = 0
    y: int = 0


class MoveBehaviour(abc.ABC):

    def __init__(self) -> None:
        self.coordinates = UnitCoordinates()
        self.target_coordinates = UnitCoordinates()
        self.is_moving: bool = False

    def move_to(self, x: int, y: int) -> None:
        self.is_moving = True
        self.target_coordinates.x = x
        self.target_coordinates.y = y

    def advance_position(self) -> bool:
        # do nothing if there already
        if any([
            self.coordinates.x == self.target_coordinates.x,
            self.coordinates.y == self.target_coordinates.y,
        ]):
            return True

        # x_diff =
        # hypotenuse = sqrt()

        return False


class AttackBehaviour(abc.ABC):
    pass


class Unit(abc.ABC):

    __last_index: int = 1

    @abc.abstractmethod
    def get_max_upgrade_level(self) -> int:
        raise NotImplementedError

    # @abc.abstractmethod
    # def get

    @property
    def name(self) -> str:
        return f"Unit-{self.unit_index}"

    def __init__(self) -> None:
        super().__init__()

        # index stuff
        self.unit_index = Unit.__last_index
        Unit.__last_index += 1

        # position stuff
        self.move_behaviour: MoveBehaviour = self.get_move_behaviour()

        # life & attack stuff
        # TODO: unfinished
        # self.life_points = 100
        # self.
        # self.attack_behaviour


# KNIGHT inheritance tree
class Knight(Unit, metaclass=abc.ABCMeta):
    pass


class TeutonicKnight(Knight):
    pass


class JapaneseKnight(Knight):
    pass


# TREBUCHET inheritance tree
class Trebuchet(Unit, metaclass=abc.ABCMeta):
    pass


class TeutonicTrebuchet(Trebuchet):
    pass


class JapaneseTrebuchet(Trebuchet):
    pass


# game instances

@enum.unique
class Civilization(enum.IntEnum):
    TEUTONS = enum.auto()
    JAPANESE = enum.auto()


class Player:

    def __init__(
        self,
        name: str,
        civilization: Civilization,
    ):
        self.name: str = name
        self.civilization: Civilization = civilization
        self.units: Set[Union[Knight, Trebuchet]] = set()

    def add_unit(self, unit: Union[Knight, Trebuchet]) -> None:
        self.units.add(unit)


# the factories

class UnitsFactory(abc.ABC):

    def __init__(self, player: Player):
        self.player = player

    @abc.abstractmethod
    def get_associated_civilization(self) -> Civilization:
        raise NotImplementedError

    @abc.abstractmethod
    def create_knight(self) -> Knight:
        raise NotImplementedError

    @abc.abstractmethod
    def create_trebuchet(self) -> Trebuchet:
        raise NotImplementedError


class TeutonicUnitsFactory(UnitsFactory):

    def get_associated_civilization(self) -> Civilization:
        return Civilization.TEUTONS

    def create_knight(self) -> TeutonicKnight:
        return TeutonicKnight()

    def create_trebuchet(self) -> TeutonicTrebuchet:
        return TeutonicTrebuchet()


class JapaneseUnitsFactory(UnitsFactory):

    def get_associated_civilization(self) -> Civilization:
        return Civilization.JAPANESE

    def create_knight(self) -> JapaneseKnight:
        return JapaneseKnight()

    def create_trebuchet(self) -> JapaneseTrebuchet:
        return JapaneseTrebuchet()


if __name__ == "__main__":

    teuton_player = Player(
        "Otto von Bismark",
        civilization=Civilization.TEUTONS
    )
    japanese_player = Player(
        "Akako Yamamoto",
        civilization=Civilization.JAPANESE
    )

    # Teutonic units
    teutonic_factory = TeutonicUnitsFactory(teuton_player)
    teutonic_knight: TeutonicKnight = teutonic_factory.create_knight()
    teutonic_trebuchet: TeutonicTrebuchet = teutonic_factory.create_trebuchet()

    # Japanese units
    japanese_factory = JapaneseUnitsFactory(japanese_player)
    japanese_knight: JapaneseKnight = japanese_factory.create_knight()
    japanese_trebuchet: JapaneseTrebuchet = japanese_factory.create_trebuchet()
