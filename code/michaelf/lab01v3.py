from turtle import *

fillcolor('green')
begin_fill()
i = 0
while i < 100:
    forward(4)
    right(360/100)
    i = i + 1
end_fill()

penup()
right(180)
forward(150)
pendown()

fillcolor('yellow')
begin_fill()
i = 0
while i < 100:
    forward(4)
    left(360/100)
    i = i + 1
end_fill()

penup()
setposition(-225, -50)
pendown()

right(180)

fillcolor('blue')
begin_fill()
i = 0
while i < 100:
    forward(4)
    left(360/100)
    i = i + 1
end_fill()

penup()
setposition(-75, -50)
pendown()

fillcolor('black')
begin_fill()
i = 0
while i < 100:
    forward(4)
    left(360/100)
    i = i + 1
end_fill()

penup()
setposition(75, -50)
pendown()

fillcolor('red')
begin_fill()
i = 0
while i < 100:
    forward(4)
    left(360/100)
    i = i + 1
end_fill()

penup()

done()