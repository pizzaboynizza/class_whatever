##  Maybe a Stick ##

from PIL import Image, ImageDraw

w = 500
h = 500
img = Image.new("RGB", (w, h))
draw = ImageDraw.Draw(img)

c_x = w / 2
c_y = h / 2
c_r = 50
draw.ellipse((c_x - c_r, c_y - c_r, c_x + c_r, c_y + c_r), fill="red")
draw.line(((250, 125), (250, 320)), fill="green")
draw.line(((200, 250), (300, 250)), fill="blue")
draw.line(((250, 320), (180, 420)), fill="pink")
draw.line(((320, 419), (250, 320)), fill="yellow")

img.show()
