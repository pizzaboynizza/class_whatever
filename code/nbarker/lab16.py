'''
Nick Barker
Lab 16
Make Lenna Greyscale
Versions 2 and 3 are bellow and denoted with a ______________________

Use the formula for converting to greyscale and the code below. Remember that Pillow uses ints for RGB values, in the range of 0-255, whereas your math will often use floats. 'Y' is used to represent the brightness. The following formula get the brightness of an RGB triplet. To convert to greyscale, set R, G, and B to Y.
'''

#Y = 0.299*R + 0.587*G + 0.114*B

from PIL import Image

r = 0
b = 0
g = 0

img = Image.open('lenna.png') # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        red = int(.299*r) 
        green = int(.587*g)
        blue = int(.114*b)
        y = red + blue + green
        #print(y)
        r = y
        g = y
        b = y
        pixels[i, j] = (r, g, b)

img.show()

'''
#___________________________Version 2, This will change the saturation for the entire photo
#open the file!
img = Image.open('lenna.png') # must be in same folder
width, height = img.size #sizes of the image
pixels = img.load() 


#get the r,g,b for each pixel
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        
        h = float(r/255)
        s = float(g/255)
        v = float(b/255)

        r, g, b, = colorsys.hsv_to_rgb(h, s, v) 
        
        #floats when they're integers 

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        pixels[i, j] = (r, g, b)
        # print(red, green, blue)
        #print("We made it past part 1!")

img.show()

# for i in range(width):
#     for j in range(height):
#         h, s, v = pixels[i, j]
#         h = int(red/255)
#         s = int(green/255)
#         v = int(blue/255)
#         pixels[i, j] = (h, s, v)

#lets select some space and change the saturation!
print(h, s, v)
img.show()
print("We made it to part 2!")

'''
#_______V2 part2____________This will draw some awesome 90s rectanges with the colors skewed in these areas only, pretty rad!  THIS WOULD BE VERSION 2.1
for i in range(300, 400):  #select a size
    for j in range(50, 500):     #select the other dimension
        h, s, v = pixels[i, j]   #we are taking HSV to Pixels!
        h = int(h+1.1)           #we 
        s = int(s+1.1)           #are
        v = int(v+1000)           #changing these
        pixels[i, j] = (h, s, v)     #back to HSV!
for i in range(width):                  #select asize
    for j in range(250, 300):           #select the other dimension
        h, s, v = pixels[i, j]          #HSV to pixels!
        h = int(h+-111)              #we
        s = int(s)                   #are
        v = int(v)                  #changing these
        pixels[i, j] = (h, s, v)   #back to HSV!
for i in range(250, i):
    for j in range(21, 162):
        h, s, v = pixels[i, j]
        h = int(h-11)
        s = int(s+100)
        v = int(v)
        pixels[i, j] = (h, s, v)
r, g, b = colorsys.hsv_to_rgb(h, s, v)
for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
        red = int(r)
        green = int(g)
        blue = int(b)
        pixels[i, j] = (r, g, b)
#print(r, g, b)
img.show()

#_________________Version 3!
'''
Lab 16
Version 3
'''

from PIL import Image, ImageDraw


width = 500
height = 500

img = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(img)

circle_x = width/2   #the head!
circle_y = height/4
circle_radius = 100
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='red')

draw.rectangle(((240, 30), (265, 350)), fill="red")  #240, 30   265,350
#draw.rectangle(((125, 250), (375, 220)), fill="pink") #125, 250  375,200
draw.line((250, 310, 425, 150), fill=('pink'), width=20)  #arm
draw.line((250, 310, 75, 150), fill=('pink'), width=20)  #arm
draw.line((370, 440, 250, 350), fill=('red'), width=30) #leg
draw.line((130, 440, 250, 350), fill=('red'), width=30) #leg
draw.line(((180, 160), (200, 180), (240, 189), (250, 197), (260, 189), (300, 180), (320, 160)), fill=("yellow"), width=10) #smile! I DID NOT SEE ARC UNTIL NOW OMGGGGGGGGGGG

img.show()