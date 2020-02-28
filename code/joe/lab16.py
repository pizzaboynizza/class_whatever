# Lab 16 (version 1)
# Author : Joe

from PIL import Image

img = Image.open("data/Lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        bright = int(0.299*g + 0.587*r + 0.114*b)

        pixels[i, j] = (bright, bright, bright)

img.show()