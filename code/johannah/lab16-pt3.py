from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

# draw.rectangle(((0, 0), (width, height)), fill="white")

# # draw a rectangle from x0, y0 to x1, y1
# draw.rectangle(((100, 100), (300, 300)), fill="lightblue")

# draw a line from x0, y0, x1, y1
# # using the color pink
# color = (256, 128, 128)  # pink
# draw.line((225, 225, width, height))
# draw.line((0, height, width, 0))

draw.line((225, 225, 150, 300))

# draw.line((150, 200, 100, 300))

# draw.line((150, 175, 200, 300))

# draw.line((250, 200, 100, 300))

# draw.line((250, 175, 200, 300))

# draw.line((150,300, 50, 450))

# draw.line((150, 300, 250, 400))


circle_x = width/2
circle_y = height/2
circle_radius = 30
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius))

img.show()