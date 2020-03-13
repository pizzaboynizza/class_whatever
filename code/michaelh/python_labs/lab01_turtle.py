"""
# Lab 1: Turtle

## Explanation

Turtle is a python `module` that allows us to move a virtual turtle around the screen using programming statements. This turtle has a position and a heading. Below are a list of commands, you can more in the [turtle docs](https://docs.python.org/3.6/library/turtle.html).

- `forward(distance)` moves the turtle forward the given number of pixels 
- `left(angle)` and `right(angle)` turns the turtle left or right by the given angle (in degrees)
- `color(color_name)` sets the pen's color, which can be `penup()` `penup()` `penup()`
- `penup()` raises the pen, a line won't be drawn when the turtle moves, `pendown()` lowers the pen again

- `setposition(x, y)` moves the turtle to the given position

- `fillcolor(color_name)` sets the fill color, `begin_fill()` indicates you'd like to begin filling in whatever you draw, `end_fill()` actually fills the shape in.

Use these functions to draw a stick figure with a head, body, two arms, and two legs. Once you're done, go through 
the examples below and create your own drawing.
"""
from turtle import *

# scale = 0.5
# # forward(scale*200)
# # left(90)
# # forward(scale*200)
# # left(90)
# # forward(scale*200)
# # left(90)
# # forward(scale*200)
# # left(90)
# # forward(scale*100)
# i=0
# fillcolor("red")
# begin_fill()
# while i < 100:
#     forward(scale*5)
#     left(360/100)
#     i=i+1
# end_fill()

# right(90)
# forward(scale*400)
# left(30)
# forward(scale*300)
# right(180)
# forward(scale*300)
# left(120)
# forward(scale*300)
# right(180)
# forward(scale*300)
# left(30)
# forward(scale*300)
# left(165)
# forward(scale*200)
# left(180)
# forward(scale*200)
# right(150)
# forward(scale*200)
# right(180)

i=0
# begin_fill()

forward(30)
speed(10)
for i in range(6):
    right(60)
    forward(30)
    right(60)
    forward(30)
    right(180)
    forward(30)

penup()
setposition(0,0)
pendown()
right(90)

i=0
while i < 200:
    forward(1.9)
    left(360/200)
    i=i+1

penup()
setposition(-5,0)
pendown()

i=0
while i < 200:
    forward(2.1)
    left(360/200)
    i=i+1


# 

# penup()
# setposition(0,5)
# pendown()

# i=0
# while i < 100:
#     forward(4.6)
#     left(360/100)
#     i=i+1


# left(90)
# forward(20)
# right(60)
# forward(20)


done()