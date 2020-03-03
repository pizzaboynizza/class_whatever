# from PIL import Image, ImageDraw
# from random import randint

# width = 500
# height = 800
# thick = 10

# img = Image.new("RGB", (width, height), color="white")

# draw = ImageDraw.Draw(img)


# # Head
# head_x = width/2 #250
# head_r = 100
# head_y = head_r + 2 * thick
# draw.ellipse((head_x-head_r, head_y-head_r, head_x+head_r, head_y+head_r), outline="black", width=thick)

# # Body
# body_x = head_x
# body_y = head_y + head_r
# body_len = head_r * 3
# draw.line((body_x, body_y, body_x, body_y+body_len), fill="black", width=thick)

# # Legs
# leg_len = body_len // 1.25
# leg_y = body_y + body_len
# leg_angle = head_r // 2 # <-> horizontal distance
# draw.line((body_x, leg_y, body_x-leg_angle, leg_y+leg_len), fill="black", width=thick) # left
# draw.line((body_x, leg_y, body_x+leg_angle, leg_y+leg_len), fill="black", width=thick) # right

# # Arms
# arm_len = body_len // 2.125
# arm_y = body_y + body_len // 5
# arm_angle = head_r // 1.125
# draw.line((body_x, arm_y, body_x-arm_angle, arm_y+arm_len), fill="black", width=thick)
# draw.line((body_x, arm_y, body_x+arm_angle, arm_y+arm_len), fill="black", width=thick)

# # Eyes
# eye_len = head_r // 2
# eye_wid = head_r // 4
# draw.line((head_x-eye_wid, head_y, head_x-eye_wid, head_y-eye_len), fill="black", width=thick)
# draw.line((head_x+eye_wid, head_y, head_x+eye_wid, head_y-eye_len), fill="black", width=thick)

# # Mouth
# mouth_len = head_r // 1.25
# mouth_x = head_x - mouth_len // 2
# mouth_y = body_y - head_r // 2
# draw.line((mouth_x, mouth_y, mouth_x+mouth_len, mouth_y), fill="black", width=thick)

# img.show()





