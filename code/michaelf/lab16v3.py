from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)


# the origin (0, 0) is at the top-left corner

draw.rectangle(((0, 0), (width, height)), fill= "white")
# draw.rectangle(((0, 0), (100, 100)), fill= "red")
# draw a rectangle from x0, y0 to x1, y1
# draw.rectangle(((100, 100), (300, 300)), fill="lightblue")
# draw.line((0, 0, 100, 100), fill = 'pink')
# draw a line from x0, y0, x1, y1
# using the color pink
color = (256, 128, 128)  # pink
# draw.line((width/2, height/2, width/2 + (width/5), height/2 + (width/5)), fill='black')
# draw.line((0, height, width, 0), fill=color)
draw.line((width/2, height/2, width/2 - (width/5), height/2 - (width/5)), fill='black')
draw.line((width/2, height/2, width/2 + (width/5), height/2 - (width/5)), fill='black')

draw.line((width/2, height/2, width/2 + (width/5), height/2 + (width/5)), fill='black')
draw.line((width/2, height/2, width/2 - (width/5), height/2 + (width/5)), fill='black')
# draw.line((width/2, height/2, width/2 + (width/5), height/5 + (width/5)), fill='black')
circle_x = width/2
circle_y = height/5
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='lightgreen')

draw.line((width/2, height/5 + 50, width/2, height/2), fill= 'black')
img.show()