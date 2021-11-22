import os
from PIL import Image

bla = os.getcwd()

im1 = Image.open("3.jpg")

im1.thumbnail((1000, 1000))

im1.save("bla.jpg")
