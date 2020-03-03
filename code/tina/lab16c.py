from PIL import Image, ImageDraw
width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)

# the origin (0, 0) is at the top-left corner

# draw.rectangle(((0, 0), (width, height)), fill="white")

# draw.line(5,6)

# draw a rectangle from x0, y0 to x 1, y1

body_x = width/2
body_y = 100
body_r = 40
draw.rectangle(body_x-body_r, body_y-body_r, body_x+body_r, body_y+body_r)

# draw.line((34,85),fill="yellow")




# circle_x = width/2
# circle_y = height/2
# circle_radius = 40
# draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')







img.show()