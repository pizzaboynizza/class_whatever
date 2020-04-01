#Something to stare at. :)  
from turtle import *
import random
bgcolor("black")
colors = ['red','orange','yellow',"green",'blue','indigo','violet','black']


for x in range(1080):
    pencolor(colors[x%7])
    width(x/300+20)
    forward(x)
    left(59)


done()