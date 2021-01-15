
from dataclasses import dataclass

import pytest
from pytest_bdd import scenario, given, when, then


def set_potato_position_in_ground(potato):
    potato.is_underground = True


def apply_water_to_potato(potato):
    potato.is_watered = True


@dataclass
class Potato:
    is_mature: bool = False
    is_round: bool = False
    is_watered: bool = False
    is_underground: bool = False
    is_growing: bool = False

    def grow(self):
        self.is_growing = self.is_watered and self.is_underground


@pytest.fixture()
def potato():
    return Potato()

@scenario('s1.feature', 'Planting the potato')
def test_plating():
    pass

@given("A mature potato")
def mature_potato(potato):
    potato.is_mature = True

@given("Potato is round")
def round_potato(potato):
    potato.is_round = True

@when("I put the potato in the ground")
def put_potato_in_the_ground(potato):
    set_potato_position_in_ground(potato)

@when("I water it")
def water_potato(potato):
    apply_water_to_potato(potato)

@then("Potato grows into a plant")
def potato_plant_grows(potato):
    potato.grow()

    print(potato)

    assert potato.is_mature
    assert potato.is_round
    assert potato.is_watered
    assert potato.is_underground
    assert potato.is_growing
