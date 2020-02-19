from turtle import *

#give the
#turtle instructions

from turtle import *

fillcolor('blue')
speed(10)

n_sides = 11
edge_length = 0

i = 0
begin_fill()
while i < 1000000:
	forward(edge_length)
	right(720/n_sides)
	i = i + 1
	edge_length = edge_length + 1
end_fill()

done()



