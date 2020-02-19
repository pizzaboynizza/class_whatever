from turtle import *

fillcolor('blue')
begin_fill()
i = 0
while i < 100:
    forward(2)
    left(360/100)
    i = i + 1
end_fill()

right(90)
forward(100)
left(45)
forward(60)

penup()
setposition(0, -100)

pendown()
right(90)
forward(60)

penup()
setposition(0, -50)

pendown()
right(90)
forward(60)

penup()
setposition(0, -50)

pendown()
right(90)
forward(60)

penup()
setposition(0, -100)
left(45)





done()

#give the turtle instructions
#done() function lets turtle do its thing