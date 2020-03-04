from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)



draw.rectangle(((0, 0), (width, height)), fill= "green")


circle_x = width/2
circle_y = height/5
circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='purple')



draw.line((width/2, height/2, width/2 + (width/2), height/2 + (width/6)), fill='red')
draw.line((width/2, height/2, width/2 - (width/3), height/2 + (width/6)), fill='red')

draw.line((width/2, height/2, width/2 - (width/4), height/2 - (width/3)), fill='blue')
draw.line((width/2, height/2, width/2 + (width/5), height/2 - (width/3)), fill='blue')



draw.line((width/2, height/5 + 50, width/2, height/2), fill= 'black')
img.show()






