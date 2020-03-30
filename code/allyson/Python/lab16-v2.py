import colorsys

from PIL import Image
img=Image.open("Lenna_(test_image).png")
width,height=img.size
pixels=img.load()

for i in range(width):
    for j in range(height):
        r, g, b= pixels[i,j]
        # r=25
        # g=87
        # b=145
        h, s, v = colorsys.rgb_to_hsv(r/25, g/87, b/145)
        r, g, b= colorsys.hsv_to_rgb(h, s, v)
        r = int(r*255)
        g = int(g*255)
        b = int(b*255)
        # print(pixels[i,j])
        pixels[i, j] = (r, g, b)










img.show()