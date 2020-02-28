# Lab 16 (version 2)
# Author : Joe

from PIL import Image
import colorsys

img = Image.open("data/Lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        h += 0.25 # rotate hue
        if h > 1.0:
            h -= 1.0

        s += 0.25 # increase saturation
        if s > 1.0:
            s = 1.0

        v -= 0.25 # decrease brightness
        if v < 0.0:
            v = 0.0

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)
    
img.show()