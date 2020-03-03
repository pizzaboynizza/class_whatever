# y=0.299*R + 0.586*G + 0.114*B

from PIL import Image
img=Image.open("Lenna_(test_image).png")
width,height=img.size
pixels=img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i,j]
        r=255
        g=255
        b=255
        # print(pixels[i,j])
        pixels[i, j] = (r, g, b)

img.show()