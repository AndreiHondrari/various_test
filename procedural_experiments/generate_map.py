
from random import randint
from PIL import Image
import math

PIXEL_SIZE = 5
WIDTH = 750
HEIGHT = 750

MAX_RADIUS_FROM_CENTER = 10
MAX_DISTANCE_FROM_MAIN_CENTERS = 30

MAX_CENTERS = 5
MIN_SUBCENTERS = 3
MAX_SUBCENTERS = MIN_SUBCENTERS + 10

DEFAULT_COLOR = (0, 0, 255,)
MAX_ZONE_COLOR = (0, 255, 0,)

print("START PROCEDURAL GENERATION")

im = Image.new('RGB', (WIDTH, HEIGHT,), color=DEFAULT_COLOR)

x_size = im.size[0] // PIXEL_SIZE
y_size = im.size[1] // PIXEL_SIZE

ABS_X_C = x_size // 2
ABS_Y_C = y_size // 2

centers = [
    # (ABS_X_C, ABS_Y_C,)
]

print(f"PMATRIX: ({x_size}, {y_size})")

# generate main centers
for _ in range(MAX_CENTERS):
    c1 = randint(1, x_size - 1)
    c2 = randint(1, y_size - 1)
    centers.append((c1, c2))

# generate centers around centers
additional_centers = []
for center in centers:
    for _ in range(randint(MIN_SUBCENTERS, MAX_SUBCENTERS + 1)):
        c1 = randint(
            center[0] - MAX_DISTANCE_FROM_MAIN_CENTERS,
            center[0] + MAX_DISTANCE_FROM_MAIN_CENTERS
        )
        c2 = randint(
            center[1] - MAX_DISTANCE_FROM_MAIN_CENTERS,
            center[1] + MAX_DISTANCE_FROM_MAIN_CENTERS
        )
        additional_centers.append((c1, c2,))

centers += additional_centers

pixel_matrix = [[DEFAULT_COLOR for y in range(y_size)] for x in range(x_size)]

# generate the color matrix
for x in range(x_size):
    for y in range(y_size):
        in_radius = False

        for center in centers:

            # transpose in first quadrant
            a = x
            b = y

            if a < center[0]:
                a = 2 * center[0] - a

            if b < center[1]:
                b = 2 * center[1] - b

            # calculate hypothenuse
            hypothenuse = round(
                math.sqrt((center[0] - a) ** 2 + (center[1] - b) ** 2)
            )

            # compare with max radius
            in_radius = hypothenuse <= MAX_RADIUS_FROM_CENTER

            if in_radius:
                pixel_matrix[x][y] = MAX_ZONE_COLOR

        if (x, y,) in centers:
            pixel_matrix[x][y] = (255, 0, 0,)

# draw the pixels
pixels = im.load()

# block pixels
for x in range(x_size):
    for y in range(y_size):

        # actual pixels
        i_min = x * PIXEL_SIZE
        i_max = ((x + 1) * PIXEL_SIZE)
        j_min = y * PIXEL_SIZE
        j_max = ((y + 1) * PIXEL_SIZE)

        for i in range(i_min, i_max):
            for j in range(j_min, j_max):
                pixels[i, j] = pixel_matrix[x][y]

im.show()

print("DONE")
