
import pygame as pg
import sys
from draw import drawScreen, t_height, t_width, drawAllText, text_total_h, text_total_w, Button, play_buttons, button_x, button_y, title_height, button_size
from bfjppParser import parse, pCompile, printList
from bfjppGame import Turn, Game
from bfjppWeb import getPrograms, loadProgram, programName



pg.init()
print("")

size = width, height = 1200, 600

screen = pg.display.set_mode(size)
pg.font.init()
font = pg.font.SysFont("Arial", 18)
bigfont = pg.font.SysFont("Arial", 32)

p1_select = "[RANDOM]"
p2_select = "[RANDOM]"

# Load all programs and ini buttons
programs = getPrograms()
ini_buttons = {}
ini_height = 30
ini_text_width = 200
ini_y = 0
ini_x = 0
# p1, p2, print buttons
for program in programs:
    ini_buttons[program] = []
    ini_buttons[program].append(Button(f"1{program}", "p1.bmp", ini_x + ini_text_width + 10, ini_y))
    ini_buttons[program].append(Button(f"2{program}", "p2.bmp", ini_x + ini_text_width + 20 + button_size, ini_y))
    if program != "[RANDOM]" and program != "[FILE]":
        ini_buttons[program].append(Button(f"P{program}", "look.bmp", ini_x + ini_text_width + 30 + button_size * 2, ini_y))
    ini_y += ini_height
    if ini_y >= height:
        ini_y = 0
        ini_x += ini_text_width + 40 + button_size * 3 + 60

ini_buttons["$play"] = [Button("play", "play.bmp", width - button_size * 4, height - button_size * 4)] #play button




turn = 0
delay = -1
delay_val = 3

done = False

menu_buttons = []
all_games = []


STATE_INI = 0
STATE_MENU = 1
STATE_PLAY = 2

state = STATE_INI

play_game = False #when true, will auto play a game; when false, game is paused
reverse_game = False #when true, play game backwards

while True:
    pressed = None
    for event in pg.event.get(): #event handling
        if event.type == pg.QUIT: sys.exit()
        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE: sys.exit()
            elif event.key == pg.K_BACKSPACE:
                pressed = "back"
            elif state != STATE_MENU:
                if event.key == pg.K_SPACE:
                    if play_game and state == STATE_PLAY:
                        pressed = "pause"
                    else:
                        pressed = "play"
                elif event.key == pg.K_EQUALS:
                    pressed = "inc"
                elif event.key == pg.K_MINUS:
                    pressed = "dec"
                elif event.key == pg.K_TAB:
                    pressed = "reverse"
                elif event.key == pg.K_PERIOD:
                    pressed = "step"
                elif event.key == pg.K_COMMA:
                    pressed = "stepback"
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


    if state == STATE_INI:
        if pressed == None:
            pass
        elif pressed[0] == "1":
            p1_select = pressed[1:]
        elif pressed[0] == "2":
            p2_select = pressed[1:]
        elif pressed[0] == "P":
            print(pressed[1:])
            print(loadProgram(pressed[1:]))
        elif pressed == "play":
            p1_name = programName(p1_select)
            p2_name = programName(p2_select)

            p1_raw = loadProgram(p1_name)
            p2_raw = loadProgram(p2_name)

            p1 = pCompile(parse(p1_raw))
            p2 = pCompile(parse(p2_raw))

            screen.fill(0x000000)
            screen.blit(bigfont.render(f"{p1_name} vs {p2_name}", 0, (0xFF, 0xFF, 0xFF)), pg.Rect(width // 4, height // 6, 200, 60))
            pg.display.flip()

            # Play All Games
            menu_buttons = []
            # play all games and add to menu buttons as each round finishes

            all_games = []

            score = 0

            for i in range(10, 31):
                temp = Game(i, False, p1, p2)
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
                menu_buttons.append(Button(f"{i}", winner, width//3 - (15 - i) * 30, height // 3))
                screen.blit(menu_buttons[-1].img, menu_buttons[-1].getrect())
                pg.display.flip()
            # Polarized
            for i in range(10, 31):
                temp = Game(i, True, p1, p2)
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
                menu_buttons.append(Button(f"-{i}", winner, width//3 - (15 - i) * 30, height // 3 + 40))
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

    elif state == STATE_MENU:
        if pressed == None:
            pass
        elif pressed == "back":
            state = STATE_INI
        elif int(pressed) < 0: # polarity
            current_game = all_games[-int(pressed) + 11]
            state = STATE_PLAY
            last = current_game.numTurns()
        else:
            current_game = all_games[int(pressed) - 10]
            state = STATE_PLAY
            last = current_game.numTurns()

    elif state == STATE_PLAY:
        if pressed == "play":
            play_game = True
        elif pressed == "pause":
            play_game = False
        elif pressed == "reset":
            turn = 0
        elif pressed == "reverse":
            reverse_game = not reverse_game
        elif pressed == "end":
            turn = last - 1
        elif pressed == "inc":
            delay_val += 1
        elif pressed == "dec":
            if delay_val > 1:
                delay_val -= 1
        elif pressed == "back":
            state = STATE_MENU
            turn = 0
            play_game = False
            reverse_game = False
        elif pressed == "step":
            if turn < last - 1:
                turn += 1
        elif pressed == "stepback":
            if turn > 0:
                turn -= 1
        elif pressed == "bigstep":
            if turn < last - 10:
                turn += 9
            else:
                turn = last - 1
        elif pressed == "bigstepback":
            if turn > 9:
                turn -= 9
            else:
                turn = 0
        elif pressed == "save":
            current_game.save(p1_name, p2_name)


        if play_game:
            delay = (delay - 1) % delay_val #stop the game from updating so fast that a person couldn't keep up

            if delay == 0 and not reverse_game and turn < last - 1:
                turn += 1
            elif delay == 0 and reverse_game and turn > 0:
                turn -= 1
            elif delay == 0: #the game has come to an end, pause
                play_game = False


        

    
    # Display
    screen.fill(0x000000)

    if state == STATE_PLAY:
        screen.blit(font.render(f"{current_game.title()} ({p1_name} vs {p2_name})", 0, (0xFF, 0xFF, 0xFF)), pg.Rect(0, 0, 200, title_height))
        screen.blit(drawScreen(current_game.history[turn].tape, current_game.history[turn].p1_pos, current_game.history[turn].p2_pos), pg.Rect(0, title_height, t_width, t_height)) #graphics of game
        screen.blit(drawAllText(current_game, turn, font), pg.Rect(0, t_height + title_height, text_total_w, text_total_h)) #text representation of game, with near history and future
        for button in play_buttons:
            screen.blit(button.img, button.getrect())
        screen.blit(font.render(f"{'Reversed'if reverse_game else 'Normal'}", 0, (0x80, 0xFF, 0x80)), pg.Rect(button_x(2), button_y(2), 80, 30))
        screen.blit(font.render(f"Delay = {delay_val}", 0, (0, 0, 0xE0)), pg.Rect(button_x(3), button_y(3), 50, 30))

    elif state == STATE_MENU:
        screen.blit(bigfont.render(f"{p1_name} vs {p2_name}", 0, (0xFF, 0xFF, 0xFF)), pg.Rect(width // 4, height // 6, 200, 60))
        screen.blit(bigfont.render(score_string, 0, (0xFF, 0xFF, 0xFF)), pg.Rect(width//3, 4 * height//6, 200, 60))
        for button in menu_buttons:
            screen.blit(button.img, button.getrect())

    elif state == STATE_INI:
        # Render Ini menu
        ini_y = 0
        ini_x = 0
        for program in programs:
            temp_x = ini_x + ini_text_width + 40 + button_size * 3
            screen.blit(font.render(program, 0, (0xFF, 0xFF, 0xFF)), pg.Rect(ini_x, ini_y, ini_text_width, ini_height))
            for button in ini_buttons[program]:
                screen.blit(button.img, button.getrect())
            if p1_select == program:
                screen.blit(font.render(" P1", 0, (0xFF, 0x0, 0x0)), pg.Rect(temp_x, ini_y, 30, ini_height))
                temp_x += 10 + button_size
            if p2_select == program:
                screen.blit(font.render(" P2", 0, (0x0, 0x0, 0xFF)), pg.Rect(temp_x, ini_y, 30, ini_height))
            ini_y += ini_height
            if ini_y >= height:
                ini_y = 0
                ini_x += ini_text_width + 40 + button_size * 3 + 70
        screen.blit(ini_buttons["$play"][0].img, ini_buttons["$play"][0].getrect())

    pg.display.flip()

