from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

draw.ellipse((110, 110, 200, 200), fill=(255, 0, 0), outline=(0, 0, 0))

color = (255, 0, 0)  

draw.line((150, 200, 150, 300), fill=color)

draw.line((150, 200, 100, 300), fill=color)

draw.line((150, 175, 200, 300), fill=color)

draw.line((250, 200, 100, 300), fill=color)

draw.line((250, 175, 200, 300), fill=color)

draw.line((150,300, 50, 450), fill=color)

draw.line((150, 300, 250, 400), fill=color)


# draw.rectangle(((100, 100)

img.show()

from PIL import Image, ImageDraw
from random import randint

width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

for i in range(1000):
    x0 = randint(0, width)
    y0 = randint(0, height)
    x1 = randint(0, width)
    y1 = randint(0, height)
    line_width = randint(1, 40)
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    draw.line((x0, y0, x1, y1), fill=(red, green, blue), width=line_width)

img.show()