#Lab 1
from turtle import *

def stickman():
    #ini
    penup()
    setposition(200, 100)
    # left(90)
    # forward(100)
    # right(90)
    pendown()
    #head
    for i in range(360):
        forward(1)
        left(1)
    forward(1)
    #eyes
    penup()
    left(90)
    forward(90) #goto top of eyes
    left(90)
    forward(20) #left eye
    left(90)
    pendown()
    forward(30) #draw left eye
    penup()
    left(180)
    forward(30)
    right(90)
    forward(40) #right eye
    right(90)
    pendown()
    forward(30) #draw right eye
    penup()
    left(180)
    forward(30)
    left(90)
    forward(20)
    left(90) #middle of face, pointing down
    #mouth
    forward(60)
    left(90)
    forward(35)
    left(180)
    pendown()
    forward(70)
    penup()
    left(180)
    forward(35)
    right(90)
    forward(30)
    pendown()
    #body
    forward(225)
    #arms
    left(180)
    forward(175)
    left(120)
    forward(100)
    left(180)
    forward(100)
    left(300)
    forward(100)
    left(180)
    forward(100)
    left(120)
    forward(175)
    #legs
    left(30)
    forward(150)
    left(180)
    forward(150)
    left(120)
    forward(150)
    right(150)
    #done

sqrsize = 10
qrsize = 37
qrneg = (qrsize * sqrsize // 2) * -1 - 100
qrpos = (qrsize * sqrsize // 2) - 100

qrcode = """
1111111010010010101111110001101111111
1000001010010100010001000011101000001
1011101001000001100100010111001011101
1011101010001100110000100111001011101
1011101011110011011110001001101011101
1000001000100111010010100011101000001
1111111010101010101010101010101111111
0000000001101010000010010110000000000
1100110101000110010001111010001101111
0001011100011111000101101011010001011
0001101000000110100111101101001000111
0110100001101000011010000110100101100
1011010010110100101101001011011100001
1110100111101001101111110111100010101
0010110100111001001000110000001011001
0010001100100010000000100010000011000
0010101001000100111110010001101101011
0000100011001100010000001000100100010
0010000011111010101100100001001001001
1110110111011100110110011111110110101
1000001100000011101111111111011000111
1100010001001100010000001000110100010
0001110010010001010111011110011110110
0010001000100011001000110001000011010
1101011011000110110001111000011110110
1111001101010011001110111111000011101
1010011001101110111010110010101001011
0000100100100010011100100000000101000
0011111110110011101110011010101011001
0010100010001100000111111101000000000
1000101011011101100001010100001111111
0001100011100101100011010100101000001
1111111110111011001000110010001011101
0001111110111010101001001101101011101
0100000011001000100010001100101011101
1011010010101110100010001010101000001
1101010110101111110111011101101111111
"""

def sqrdraw():
    pendown()
    begin_fill()
    forward(sqrsize)
    left(90)
    forward(sqrsize)
    left(90)
    forward(sqrsize)
    left(90)
    forward(sqrsize)
    left(90)
    end_fill()
    penup()

def drawqr():
    pos = 1
    penup()
    for x in range(qrneg, qrpos, sqrsize):
        for y in range(qrneg, qrpos, sqrsize):
            setposition(x, y)
            if qrcode[pos] == "1":
                sqrdraw()
            pos += 1
        pos += 1

def stardraw(x, y, color, size):
    penup()
    setposition(x, y)
    pendown()
    edge_length = 0
    fillcolor(color)
    begin_fill()
    for i in range(size):
        forward(edge_length)
        right(144)
        edge_length += 4
    right(2)
    forward(edge_length)
    end_fill()

speed(0)

stickman()

drawqr()

stardraw(-150, 250, "red", 20)
stardraw(0, 190, "green", 22)
stardraw(-260, 235, "blue", 18)
stardraw(100, 260, "yellow", 17)

done()

