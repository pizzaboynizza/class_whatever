from turtle import *
left(45)
forward(100)
left(-90)
forward(100)
penup()
backward(100)
left(135)
pendown()
forward(100)

left(45)
backward(100)
penup()
forward(100)
left(135)
pendown()
left(-45)
forward(100)
left(180)
penup()
forward(100)
left(45)
pendown()
right(90)

i = 0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1

done()