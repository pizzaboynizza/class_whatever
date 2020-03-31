# Pillow can also be used to draw, the code below demonstrates some functions that Pillow provides. Use these functions to draw a stick figure. You can find more documentation here.

from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)




color = (255, 255, 255)  

draw.ellipse((110, 110, 200, 200), fill=color)
draw.line((150, 200, 150, 300), fill=color)

draw.line((150, 200, 100, 250), fill=color)

draw.line((150, 200, 200, 250), fill=color)

# draw.line((250, 200, 100, 300), fill=color)

# draw.line((250, 175, 200, 300), fill=color)

draw.line((150,300, 50, 450), fill=color)

draw.line((150, 300, 250, 400), fill=color)


# draw.rectangle(((100, 100)

img.show()

# circle_x = width/2
# circle_y = height/2
# circle_radius = 100
# draw.ellipse(circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius)

img.show()
