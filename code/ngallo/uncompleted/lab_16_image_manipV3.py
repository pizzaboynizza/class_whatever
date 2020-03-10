from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

from graphics import *
win = GraphWin("Stick figure")
head = Circle(Point(100, 60), 20).draw(win)
body = Line(Point(100, 80), Point(100, 120)).draw(win)
arms= Line(Point(60, 100), Point(140, 100)).draw(win)
leg1 = Line(Point(100,120), Point(60,160)).draw(win)
leg2 = Line(Point(100,120), Point(140,160)).draw(win)

'''
Version 3
Pillow can also be used to draw, the code below demonstrates some functions that Pillow provides. Use these functions to draw a stick figure. You can find more documentation here.

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill="white")

# draw a rectangle from x0, y0 to x1, y1
draw.rectangle(((100, 100), (300, 300)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
draw.line((0, 0, width, height), fill=color)
draw.line((0, height, width, 0), fill=color)


circle_x = width/2
circle_y = height/2
circle_radius = 100
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

img.show()
Try running the code below, which generates 1000 random lines with random colors.

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

'''