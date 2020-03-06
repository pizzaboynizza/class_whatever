from PIL import Image, ImageDraw

width = 500
height = 500

img = Image.new('RGB', (width, height))

draw = ImageDraw.Draw(img)



color = ('white')


circle_x = width/4
circle_y = height/4
circle_radius = 50

# circle_x = width/2
# circle_y = height/4
# circle_radius = 50
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='white')
draw.line(((475,0), (width, height)), fill="black")
# draw.line((0, 0, width, height), fill=color)
# draw.line((5, 0, height, width), fill=color)
# draw.line((10, 0, width, height), fill=color)
# draw.line((15 0, height, width), fill=color)
circle_x = width/4
circle_y = height/4
circle_radius = 85
draw.ellipse((circle_x-circle_radius, circle_y-circle_radius, circle_x+circle_radius, circle_y+circle_radius), fill='black')
draw.line(((460,50,width,height)), fill='black')
draw.line(((00, 50,width, height)), fill="red")
draw.line(((10, 50,width, height)), fill="orange")
draw.line(((20, 50,width, height)), fill="yellow")
draw.line(((30, 50,width, height)), fill="green")
draw.line(((40, 50,width, height)), fill="blue")
draw.line(((50, 50,width, height)), fill="indigo")
draw.line(((60, 50,width, height)), fill="violet")
draw.line(((70, 50,width, height)), fill="red")
draw.line(((80, 50,width, height)), fill="orange")
draw.line(((90, 50,width, height)), fill="yellow")
draw.line(((100, 50,width, height)), fill="green")
draw.line(((110, 50,width, height)), fill="blue")
draw.line(((120, 50,width, height)), fill="indigo")
draw.line(((130, 50,width, height)), fill="violet")
draw.line(((140, 50,width, height)), fill="red")
draw.line(((150, 50,width, height)), fill="orange")
draw.line(((160, 50,width, height)), fill="yellow")
draw.line(((170, 50,width, height)), fill="green")
draw.line(((180, 50,width, height)), fill="blue")
draw.line(((190, 50,width, height)), fill="indigo")
draw.line(((200, 50,width, height)), fill="violet")
draw.line(((210, 50,width, height)), fill="red")
draw.line(((220, 50,width, height)), fill="orange")
draw.line(((230, 50,width, height)), fill="yellow")
draw.line(((240, 50,width, height)), fill="green")
draw.line(((250, 50,width, height)), fill="blue")
draw.line(((260, 50,width, height)), fill="indigo")
draw.line(((270, 50,width, height)), fill="violet")
draw.line(((280, 50,width, height)), fill="red")
draw.line(((290, 50,width, height)), fill="orange")
draw.line(((300, 50,width, height)), fill="yellow")
draw.line(((310, 50,width, height)), fill="green")
draw.line(((320, 50,width, height)), fill="blue")
draw.line(((330, 50,width, height)), fill="indigo")
draw.line(((340, 50,width, height)), fill="violet")
draw.line(((350, 50,width, height)), fill="red")
draw.line(((360, 50,width, height)), fill="orange")
draw.line(((370, 50,width, height)), fill="yellow")
draw.line(((380, 50,width, height)), fill="green")
draw.line(((390, 50,width, height)), fill="blue")
draw.line(((400, 50,width, height)), fill="indigo")
draw.line(((410, 50,width, height)), fill="violet")
draw.line(((420, 50,width, height)), fill="red")
draw.line(((430, 50,width, height)), fill="orange")
draw.line(((440, 50,width, height)), fill="yellow")
draw.line(((450, 50,width, height)), fill="green")
draw.line(((460, 50,width, height)), fill="blue")
draw.line(((470, 50,width, height)), fill="indigo")
draw.line(((480, 50,width, height)), fill="violet")
draw.line(((490, 50,width, height)), fill="red")
draw.line(((500, 50,width, height)), fill="orange")
draw.line(((510, 50,width, height)), fill="yellow")
draw.line(((520, 50,width, height)), fill="green")
draw.line(((530, 50,width, height)), fill="blue")
draw.line(((540, 50,width, height)), fill="indigo")
draw.line(((550, 50,width, height)), fill="violet")

img.show()