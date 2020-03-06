from PIL import Image

img = Image.open("lenna.png")
width, height = img.size
pixels = img.load()

for i in range(width):
    for j in range(height):
        r, g, b = pixels[i, j]

        # # formula for converting to greyscale:
        Y = 0.299*r + 0.587*g + 0.114*b
        
        pixels[i, j] = (int(Y), int(Y), int(Y))
        #pixels[i, j] = (r, g, b)

img.show()
#img.show(Y)