import pygame as pg


title_height = 30
block_size = 20
buffer = 10 # a buffer area around my drawing spaces
t_width = 32 * block_size + buffer
t_height = 128 * 2 + block_size + buffer * 2
t_y = buffer//4 + 128 + title_height

def drawScreen(tape, p1, p2):
    ret = pg.Surface((t_width, t_height))
    tape_color = 0xFFFFFF
    for t in range(len(tape)):
        if t == 0:
            tape_color = 0xFF4040
        elif t == len(tape) - 1:
            tape_color = 0x4040FF
        else:
            tape_color = 0xFFFFFF

        tape_x = buffer//2 + (t + 1) * block_size
        
        if tape[t] == 0:
            pass
        elif tape[t] <= 128:
            pg.draw.rect(ret, tape_color, pg.Rect(tape_x, t_y, block_size, -tape[t]))
        else:
            pg.draw.rect(ret, tape_color, pg.Rect(tape_x, t_y + block_size, block_size, 128 - tape[t] % 128))

    if p1 == p2:
        pg.draw.rect(ret, 0xFF00FF, pg.Rect((p1 + 1) * block_size + buffer//2, t_y, block_size, block_size))
    else:
        pg.draw.rect(ret, 0xFF0000, pg.Rect((p1 + 1) * block_size + buffer//2, t_y, block_size, block_size))
        pg.draw.rect(ret, 0x0000FF, pg.Rect((p2 + 1) * block_size + buffer//2, t_y, block_size, block_size))
    
    return ret


def getTextLine(hist, turn, font):
    return font.render(f"{' '*(5-len(str(turn)))}{turn}:  " + str(hist), 0, (0xE0, 0, 0))

text_height = 30
text_width = 960
text_total_w = text_width + buffer
text_total_h = text_height * 9 + buffer

def drawAllText(game, turn, font):
    txt_screen = pg.Surface((text_total_w, text_total_h))
    # txt_screen.fill(0xFFFFFF) # for testing purposes
    max_turns = len(game.history) # don't want to do this function more than once if we have a long game
    y = buffer//2
    for i in range(turn-4, turn+5):
        if not (i < 0 or i >= max_turns):
            txt_screen.blit(getTextLine(game.history[i], i, font), pg.Rect(buffer//2, y, text_width, text_height))
        y += text_height
    return txt_screen

button_size = 30

class Button:
    def __init__(self, button, img, x, y):
        self.img = pg.image.load(img)
        self.type = button
        self.x = x
        self.y = y

    def iscollide(self, pos):
        return pg.Rect((self.x, self.y), self.img.get_size()).collidepoint(pos)

    def getrect(self):
        return pg.Rect((self.x, self.y), self.img.get_size())

def button_x(num): #start at one
    return t_width + num * (button_size + buffer // 2)

def button_y(num): # start at one
    return buffer * num + button_size * (num - 1) + title_height

play_buttons = [
    Button("play", "play.bmp", button_x(1), button_y(1)),
    Button("pause", "pause.bmp", button_x(2), button_y(1)),
    Button("reset", "reset.bmp", button_x(3), button_y(1)),
    Button("end", "end.bmp", button_x(4), button_y(1)),
    Button("reverse", "reverse.bmp", button_x(1), button_y(2)),
    Button("inc", "inc.bmp", button_x(1), button_y(3)),
    Button("dec", "dec.bmp", button_x(2), button_y(3)),
    Button("back", "back.bmp", button_x(6), button_y(1)),
    Button("step", "step.bmp", button_x(3), button_y(5)),
    Button("bigstep", "bigstep.bmp", button_x(4), button_y(5)),
    Button("stepback", "stepback.bmp", button_x(2), button_y(5)),
    Button("bigstepback", "bigstepback.bmp", button_x(1), button_y(5)),
    Button("save", "save.bmp", button_x(12), button_y(1))
] # play, pause, increase delay, decrease delay, reset, end, reverse, step forward, step back, big step forward, bug step back