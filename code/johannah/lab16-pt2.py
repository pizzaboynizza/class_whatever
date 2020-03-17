'''
-Use the colorsys library to Increase the Saturation, Decrease the Brightness, and Rotate the Hue
-Colorsys represents colors as floats in the range 0.0 - 1.0, whereas pillow uses ints in the range 0 - 255. You'll have to convert between these two representations.
'''

from PIL import Image
import colorsys

img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # colorsys uses colors in the range [0, 1]
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)

        # do some math on h, s, v
        h = float(h+1.2)  #rotate hue
        if h >= 1:
            h = h - 1
        s = float(s*10)  #increase saturation
        v = float(v/5)  #decrease brightness
        b = int(b)

        

        r, g, b = colorsys.hsv_to_rgb(h, s, v)

        # convert back to [0, 255]

        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        
        #pixels[i, j] = (int(Y), int(Y), int(Y))
        pixels[i, j] = (r, g, b)

img.show()