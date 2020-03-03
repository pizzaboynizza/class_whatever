#convert image into greyscale using pillow library
#download image
#install pilow
# use Y = 0.299*R + 0.587*G + 0.114*B and code to convert image to greyscale
#Use the colorsys library to increase the saturation, decrease the brightness, and rotate the hue
#import colorsys

import colorsys
from PIL import Image 
img = Image.open("test_pic.png") # must be in same folder
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]
       # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        # do some math on h, s, v
        h = h + 0.9
        s = s + 0.9
        v = v - 0.6

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]
       

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)

        pixels[i, j] = (r, g, b)

img.show()