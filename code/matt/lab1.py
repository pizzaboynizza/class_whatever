# Turtle lab
from turtle import *

# Give the turtle directions

# Draw a Stick Figure

#hide annoying stupid arrow
hideturtle()


#head and neck
left(90)
forward(100)
right(90)
forward(50)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(50)

#return to start
penup()
setposition(0, 0)
pendown()

#right arm
left(45)
forward(75)

#home pos
setposition(0, 0)

#left arm
left(90)
forward(75)

#home pos
setposition(0, 0)

#body
left(135)
forward(100)

#left leg
right(45)
forward(75)

#base of body set position
setposition(0, -100)

#right leg
left(90)
forward(75)

#drawing face
#left eye
penup()
setposition(-25, 175)
pendown()
left(45)
fillcolor("green")
begin_fill()
forward(5)
right(90)
forward(5)
right(90)
forward(5)
right(90)
forward(5)
end_fill()

#right eye
penup()
setposition(25, 175)
pendown()
right(90)
fillcolor("green")
begin_fill()
forward(5)
right(90)
forward(5)
right(90)
forward(5)
right(90)
forward(5)
end_fill()

#mouth
penup()
setposition(-25, 126)
pendown()
fillcolor("black")
begin_fill()
right(90)
forward(50)
right(90)
forward(2)
right(90)
forward(50)
right(90)
forward(2)
end_fill()

done()


