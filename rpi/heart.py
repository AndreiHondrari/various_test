import time
from copy import deepcopy
from sense_hat import SenseHat

shat = SenseHat()
shat.set_rotation(180)

o = (0, 0, 0,)
x = (255, 0, 0,)

DEFAULT_LED_MATRIX = [
    o, x, x, o, o, x, x, o,
    x, o, o, x, x, o, o, x,
    x, o, o, x, x, o, o, x,
    x, o, o, o, o, o, o, x,
    o, x, o, o, o, o, x, o,
    o, o, x, o, o, x, o, o,
    o, o, o, x, x, o, o, o,
    o, o, o, o, o, o, o, o,
]

START_ROW = 1
SIZE = 8

# min col = row * 8
# max col = min col + 8 -1
# 0, 1, 2, 3, 4, 5, 6, 7
# 8, 9, 10, 11, 12, 13, 14, 15
# 16
# 24
# 32
# 40
# 48
# 56


shat.set_pixels(DEFAULT_LED_MATRIX)


def fill_heart(row: int, led_matrix: list) -> list:
    led_matrix = deepcopy(led_matrix)

    for i in range(SIZE):
        if i < row:
            continue

        min_col = i * 8
        max_col = min_col + 8 - 1

        cell_active = False

        # sweep columns for row
        for i in range(min_col, max_col):
            if led_matrix[i] == x:
                cell_active = not cell_active
                continue

            led_matrix[i] = x if cell_active else o

    return led_matrix


def pump_heart() -> None:
    # inflate heart
    for i in range(START_ROW, SIZE+1):
        time.sleep(0.05)
        current_row = SIZE - i
        led_matrix = fill_heart(current_row, DEFAULT_LED_MATRIX)
        shat.set_pixels(led_matrix)

    # deflate heart
    for i in range(START_ROW, SIZE+1):
        time.sleep(0.05)
        led_matrix = fill_heart(i, DEFAULT_LED_MATRIX)
        shat.set_pixels(led_matrix)


if __name__ == "__main__":

    print("--- Heart pump ---")
    while True:
        # for i in range(3):
        pump_heart()

        # shat.show_message("kocham cie!", text_colour=(255, 255, 255,))
