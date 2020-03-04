from PIL import Image
import colorsys
img = Image.open("lenna.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        y = 0.299*r + 0.587*g + 0.114*b
        a = round(y)


        pixels[i, j] = (a,a,a)

img.show()

