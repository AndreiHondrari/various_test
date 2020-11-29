import time
import typing
from copy import deepcopy
from sense_hat import SenseHat
from abc import ABC, abstractmethod
import random
import enum

SIZE = 8

# min col = row * 8
# max col = min col + 8 -1
# 0 .. 7
# 8 .. 15
# 16 .. 23
# 24 .. 31
# 32 .. 39
# 40 .. 47
# 48 .. 55
# 56 .. 63



BLACK = [0, 0, 0,]
WHITE = [255, 255, 255,]


class LimitDimension(ABC):

    @abstractmethod
    def get_collection(self):
        raise NotImplementedError()

    def __init__(self):
        self._min_index = 0
        self._max_index = SIZE - 1

    def __getitem__(self, index):
        if index < self._min_index:
            raise IndexError()
        if index > self._max_index:
            raise IndexError()
        collection = self.get_collection()
        return collection[index]

    @property
    def min_index(self):
        return self._min_index

    @property
    def max_index(self):
        return self._max_index


class CellMode(enum.IntEnum):
    UNICOLOR = 0
    NORMAL = 1


class Cell:

    def __init__(self, value=0):
        self._mode = CellMode.UNICOLOR
        self._min = 0
        self._max = 255
        self.set(value)
        self._direction = (value != 255)
        self._countdown_active = False
        self._countdown_value = 0

    @property
    def R(self):
        return self._r

    @property
    def G(self):
        return self._g

    @property
    def B(self):
        return self._b

    @property
    def value(self):
        return [self._r, self._g, self._b]

    def set(self, color):
        if self._mode == CellMode.UNICOLOR:
            assert (
                isinstance(color, int) and
                self._min <= color <= self._max
            ), f"{color}"

            self._value = color
            self._r = color
            self._g = color
            self._b = color
        else:
            assert color is Iterable and len(color) == 3, f"{color}"

            self._r = color[0]
            self._g = color[1]
            self._b = color[2]

    def tick(self):
        assert self._mode == CellMode.UNICOLOR

        if self._countdown_value <= 0:
            self._countdown_active = False

        if self._countdown_active:
            self._countdown_value -= 1
            return

        reached_upper_limit = self._value >= self._max and self._direction
        reached_lower_limit = self._value <= self._min and not self._direction

        if reached_upper_limit:
            self._direction = False

        if reached_lower_limit:
            self._direction = True

        if reached_upper_limit or reached_lower_limit:
            self._countdown_active = True
            self._countdown_value = random.randint(50, 100)

        if self._direction:
            next_val = self._value + 5
        else:
            next_val = self._value - 5

        if next_val < self._min:
            self._value = 0
        elif next_val > self._max:
            self._value = 255
        else:
            self._value = next_val

        self.set(self._value)


class Row(LimitDimension):

    def __init__(self):
        super().__init__()
        self._collection = [Cell() for _ in range(SIZE)]

    def get_collection(self):
        return self._collection

    def __setitem__(self, index, value):
        collection = self.get_collection()
        collection[index] = value


class Matrix(LimitDimension):

    def __init__(self):
        super().__init__()
        self._collection = [Row() for j in range(SIZE)]

    def get_collection(self):
        return self._collection

    @property
    def pixels(self):
        return [
            cell.value for row in self.get_collection() for cell in row
        ]

if __name__ == "__main__":

    print("--- Matrix ---")
    shat = SenseHat()
    shat.set_rotation(180)
    matrix = Matrix()

    # initialize randomized matrix
    for i in range(SIZE):
        for j in range(SIZE):
            rand_val = random.randint(100, 150)
            matrix[i][j].set(rand_val)
            matrix[i][j]._direction = bool(random.randint(0, 1))

    shat.set_pixels(matrix.pixels)

    while True:
        time.sleep(0.01)

        for i in range(0, SIZE):
            for j in range(0, SIZE):
                matrix[i][j].tick()

        shat.set_pixels(matrix.pixels)
