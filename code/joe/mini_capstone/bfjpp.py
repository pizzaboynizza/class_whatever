# Author : Joe
# This is the main file
# external libraries used are 'pygame' and 'requests'

import pygame as pg
import sys

from draw import drawScreen, t_height, t_width, drawAllText, text_total_h, text_total_w, Button, play_buttons, button_x, button_y, title_height, button_size, showMessage
from bfjppParser import parse, pCompile, printList
from bfjppGame import Turn, Game
from bfjppWeb import getPrograms, loadProgram, programName

# TODO:
#   -Tidy up UI
#   -Comment code


pg.init()

size = width, height = 1200, 600 # size of the display window

# Initializing pygame stuff
screen = pg.display.set_mode(size)
pg.display.set_caption("BF Joust")
pg.font.init()
font = pg.font.SysFont("Arial", 18)
bigfont = pg.font.SysFont("Arial", 32)
hugefont = pg.font.SysFont("Arial", 64)

p1_select = "[RANDOM]"
p2_select = "[RANDOM]"

# Load all programs and ini buttons
programs = getPrograms()
ini_buttons = {}
ini_height = 30
ini_text_width = 200
ini_y = 0
ini_x = 0
# p1, p2, and print buttons; for each program
for program in programs:
    ini_buttons[program] = []
    ini_buttons[program].append(Button(f"1{program}", "p1.bmp", ini_x + ini_text_width + 10, ini_y))
    ini_buttons[program].append(Button(f"2{program}", "p2.bmp", ini_x + ini_text_width + 20 + button_size, ini_y))
    if program != "[RANDOM]" and program != "[FILE]": # random and file don't get a print button
        ini_buttons[program].append(Button(f"P{program}", "look.bmp", ini_x + ini_text_width + 30 + button_size * 2, ini_y))
    ini_y += ini_height
    if ini_y >= height: # when it runs out of height, move to the side and start from the top
        ini_y = 0
        ini_x += ini_text_width + 40 + button_size * 3 + 60

ini_buttons["$play"] = [Button("play", "play.bmp", width - button_size * 4, height - button_size * 4)] #play button


# Declaring some variables
turn = 0
delay = -1
delay_val = 3

menu_buttons = []
all_games = []

# Labeling my states so they are easily identifiable, and so I don't need to use strings and possibly slow things down
STATE_INI = 0
STATE_MENU = 1
STATE_PLAY = 2

state = STATE_INI

play_game = False #when true, will auto play a game; when false, game is paused
reverse_game = False #when true, play game backwards

display_update = True # when true, update the display; this way we don't update the display all the time if it is unneccesary
    # this kind of broke the delay function, so that has been modified further below

while True:
    pressed = None
    for event in pg.event.get(): #event handling
        if event.type == pg.QUIT: sys.exit()
        if event.type == pg.KEYUP: # Key presses on keyboard
            if event.key == pg.K_ESCAPE: sys.exit()
            elif event.key == pg.K_BACKSPACE:   pressed = "back"
            elif state != STATE_MENU:
                if event.key == pg.K_SPACE:
                    if play_game and state == STATE_PLAY:
                        pressed = "pause"
                    else:
                        pressed = "play"
                elif event.key == pg.K_EQUALS:  pressed = "inc"
                elif event.key == pg.K_MINUS:   pressed = "dec"
                elif event.key == pg.K_TAB:     pressed = "reverse"
                elif event.key == pg.K_PERIOD:  pressed = "step"
                elif event.key == pg.K_COMMA:   pressed = "stepback"
                elif event.key == pg.K_RETURN:  pressed = "reset"
                elif event.key == pg.K_LEFT:    pressed = "bigstepback"
                elif event.key == pg.K_RIGHT:   pressed = "bigstep"
        elif event.type == pg.MOUSEBUTTONUP: # handle mouse clicks
            mouse_pos = pg.mouse.get_pos()
            if state == STATE_PLAY:
                for button in play_buttons:
                    if button.iscollide(mouse_pos):
                        pressed = button.type
            elif state == STATE_MENU:
                for button in menu_buttons:
                    if button.iscollide(mouse_pos):
                        pressed = button.type
            elif state == STATE_INI:
                for buttons in ini_buttons.values():
                    for button in buttons:
                        if button.iscollide(mouse_pos):
                            pressed = button.type


    if state == STATE_INI: # Initial screen; shows all the programs
        if pressed == None:
            pass
        elif pressed[0] == "1":
            p1_select = pressed[1:]
            display_update = True
        elif pressed[0] == "2":
            p2_select = pressed[1:]
            display_update = True
        elif pressed[0] == "P":
            print(pressed[1:])
            print(loadProgram(pressed[1:]))
        elif pressed == "play": # Play through all games between selected programs and goto menu
            display_update = True
            p1_name = programName(p1_select, screen, hugefont)
            p2_name = programName(p2_select, screen, hugefont)

            p1_raw = loadProgram(p1_name)
            p2_raw = loadProgram(p2_name)

            showMessage("Compiling programs...", screen, hugefont, (0x0, 0xFF, 0x0), width, height//2)
            p1 = pCompile(parse(p1_raw))
            p2 = pCompile(parse(p2_raw))

            screen.fill(0x000000)
            screen.blit(bigfont.render(f"{p1_name} vs {p2_name}", 0, (0xFF, 0xFF, 0xFF)), pg.Rect(width // 4, height // 6, 200, 60))
            pg.display.flip()

            # Play All Games
            menu_buttons = []
            # play all games and add to menu buttons as each round finishes

            all_games = [] # The list of all games

            score = 0 # Total score (positive for p1, negative for p2)

            for p in range(2):
                #p=0 for not polarized, p=1 for polarized
                for i in range(10, 31):
                    temp = Game(i, False if p == 0 else True, p1, p2)
                    temp.play()
                    all_games.append(temp)
                    winner = temp.winner
                    if winner == "Tie Game":
                        winner = "tie.bmp"
                    elif winner == "P1 Wins":
                        score += 1
                        winner = "left.bmp"
                    else:
                        score -= 1
                        winner = "right.bmp"
                    menu_buttons.append(Button(f"{'-' if p == 1 else ''}{i}", winner, width//3 - (15 - i) * 30, height // 3 + (40 if p == 1 else 0)))
                    screen.blit(menu_buttons[-1].img, menu_buttons[-1].getrect())
                    pg.display.flip()

            score_string = ""
            if score > 0:
                score_string = f"{p1_name} wins ({score})"
            elif score < 0:
                score_string = f"{p2_name} wins ({score})"
            else:
                score_string = f"Tie game ({score})"

            menu_buttons.append(Button("back", "back.bmp", 5 * width // 6, 10))
            
            state = STATE_MENU

    elif state == STATE_MENU: # Menu screen; look at overveiw of all games between programs
        if pressed == None:
            pass
        elif pressed == "back": # go back to ini menu
            display_update = True
            state = STATE_INI
        elif int(pressed) < 0: # polarity
            display_update = True
            current_game = all_games[-int(pressed) + 11]
            state = STATE_PLAY
            last = current_game.numTurns()
        else:
            display_update = True
            current_game = all_games[int(pressed) - 10]
            state = STATE_PLAY
            last = current_game.numTurns()

    elif state == STATE_PLAY: # Play screen; look at and step through a specific game
        if pressed == "play": # play the game
            play_game = True
        elif pressed == "pause": # pause the game
            play_game = False
        elif pressed == "reset": # goto first turn
            turn = 0
            display_update = True
        elif pressed == "reverse": # reverse the game (play it backwards)
            reverse_game = not reverse_game
            display_update = True
        elif pressed == "end": # goto final turn
            turn = last - 1
            display_update = True
        elif pressed == "inc": # increase delay
            delay_val += 1
            display_update = True
        elif pressed == "dec": # decrease delay
            if delay_val > 0:
                delay_val -= 1
                display_update = True
        elif pressed == "back": # go back to menu
            state = STATE_MENU
            turn = 0
            play_game = False
            reverse_game = False
            display_update = True
        elif pressed == "step": # goto next turn
            if turn < last - 1:
                turn += 1
                display_update = True
        elif pressed == "stepback": # goto previous turn
            if turn > 0:
                turn -= 1
                display_update = True
        elif pressed == "bigstep": # skip the next 9 turns
            if turn < last - 10:
                turn += 9
                display_update = True
            else:
                turn = last - 1
                display_update = True
        elif pressed == "bigstepback": # go back 9 turns
            if turn > 9:
                turn -= 9
                display_update = True
            else:
                turn = 0
                display_update = True
        elif pressed == "save": # save the game
            current_game.save(p1_name, p2_name, screen, hugefont)
            display_update = True


        if play_game:
            delay = (delay - 1) % (delay_val * 800 if delay_val > 0 else 1) #stop the game from updating so fast that a person couldn't keep up

            if delay == 0 and not reverse_game and turn < last - 1:
                turn += 1
                display_update = True
            elif delay == 0 and reverse_game and turn > 0:
                turn -= 1
                display_update = True
            elif delay == 0: #the game has come to an end, pause
                play_game = False


        

    if display_update:
        # Display
        screen.fill(0x000000)

        if state == STATE_PLAY: # Play screen display
            screen.blit(font.render(f"{current_game.title()} ({p1_name} vs {p2_name})", 0, (0xFF, 0xFF, 0xFF)), pg.Rect(0, 0, 200, title_height)) #title of game (tape length, polarity, programs)
            screen.blit(drawScreen(current_game.history[turn].tape, current_game.history[turn].p1_pos, current_game.history[turn].p2_pos), pg.Rect(0, title_height, t_width, t_height)) #graphics of game
            screen.blit(drawAllText(current_game, turn, font), pg.Rect(0, t_height + title_height, text_total_w, text_total_h)) #text representation of game, with near history and future
            for button in play_buttons: # all buttons
                screen.blit(button.img, button.getrect())
            screen.blit(font.render(f"{'Reversed'if reverse_game else 'Normal'}", 0, (0x80, 0xFF, 0x80)), pg.Rect(button_x(2), button_y(2), 80, 30)) # reverse status
            screen.blit(font.render(f"Delay = {delay_val}", 0, (0, 0, 0xE0)), pg.Rect(button_x(3), button_y(3), 50, 30)) # delay status

        elif state == STATE_MENU: # Menu screen display
            screen.blit(bigfont.render(f"{p1_name} vs {p2_name}", 0, (0xFF, 0xFF, 0xFF)), pg.Rect(width // 4, height // 6, 200, 60)) # program names
            screen.blit(bigfont.render(score_string, 0, (0xFF, 0xFF, 0xFF)), pg.Rect(width//3, 4 * height//6, 200, 60)) # total results
            for button in menu_buttons: # all buttons
                screen.blit(button.img, button.getrect())
            for i in range(10, 31):
                screen.blit(font.render(str(i), 0, (0x80, 0xFF, 0x80)), pg.Rect(width//3 - (15 - i) * 30 + 8, height // 3 - 20, 30, 30))

        elif state == STATE_INI: # Inital screen display
            ini_y = 0
            ini_x = 0
            for program in programs: # all programs
                temp_x = ini_x + ini_text_width + 40 + button_size * 3
                screen.blit(font.render(program, 0, (0xFF, 0xFF, 0xFF)), pg.Rect(ini_x, ini_y, ini_text_width, ini_height)) # program name
                for button in ini_buttons[program]:
                    screen.blit(button.img, button.getrect())
                if p1_select == program:
                    screen.blit(font.render(" P1", 0, (0xFF, 0x0, 0x0)), pg.Rect(temp_x, ini_y, 30, ini_height)) # P1 selected
                    temp_x += 10 + button_size
                if p2_select == program:
                    screen.blit(font.render(" P2", 0, (0x0, 0x0, 0xFF)), pg.Rect(temp_x, ini_y, 30, ini_height)) # P2 selected
                ini_y += ini_height
                if ini_y >= height: # move left when no more room
                    ini_y = 0
                    ini_x += ini_text_width + 40 + button_size * 3 + 70
            screen.blit(ini_buttons["$play"][0].img, ini_buttons["$play"][0].getrect()) # play button

        display_update = False

        pg.display.flip()
