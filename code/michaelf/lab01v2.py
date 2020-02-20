from turtle import *

fillcolor('green')
begin_fill()
i = 0
while i < 4:
    forward(100)
    right(90)
    i = i + 1
end_fill()

right(180)
forward(50)

fillcolor('yellow')
begin_fill()
i = 0
while i < 4:
    forward(100)
    left(90)
    i = i + 1
end_fill()

penup()
setposition(-225, -50)
pendown()

right(180)

fillcolor('blue')
begin_fill()
i = 0
while i < 4:
    forward(100)
    left(90)
    i = i + 1
end_fill()

penup()
setposition(-75, -50)
pendown()

fillcolor('black')
begin_fill()
i = 0
while i < 4:
    forward(100)
    left(90)
    i = i + 1
end_fill()

penup()
setposition(75, -50)
pendown()

fillcolor('red')
begin_fill()
i = 0
while i < 4:
    forward(100)
    left(90)
    i = i + 1
end_fill()



done()