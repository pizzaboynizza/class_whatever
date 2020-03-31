## Tic Tac Toe ##
##  Reworked  ##

import time
import random


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Board:
    def __init__(self):
        self.space = {
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
        }

    def __repr__(self):
        text_board = ""
        text_board += (
            " " + self.space[1] + " | " + self.space[2] + " | " + self.space[3] + "\n"
        )
        text_board += "---|---|---\n"
        text_board += (
            " " + self.space[4] + " | " + self.space[5] + " | " + self.space[6] + "\n"
        )
        text_board += "---|---|---\n"
        text_board += (
            " " + self.space[7] + " | " + self.space[8] + " | " + self.space[9] + "\n"
        )
        return text_board

    def play(self, play, player):

        if self.chk(play) is True:
            self.space[play] = player.token
            return True
        return False

    def chk(self, key):
        if self.space[key] == "X" or self.space[key] == "O":
            print("Space in Use.")
            return False
        else:
            return True

    def check_winner(self):
        if self.space[1] == self.space[2] == self.space[3]:
            print(f"{self.space[1]} gonna give it to ya!")
            quit()
        elif self.space[4] == self.space[5] == self.space[6]:
            print(f"{self.space[4]} gonna give it to ya!")
            quit()
        elif self.space[7] == self.space[8] == self.space[9]:
            print(f"{self.space[7]} gonna give it to ya!")
            quit()
        elif self.space[1] == self.space[5] == self.space[9]:
            print(f"{self.space[1]} gonna give it to ya!")
            quit()
        elif self.space[1] == self.space[4] == self.space[7]:
            print(f"{self.space[1]} gonna give it to ya!")
            quit()
        elif self.space[2] == self.space[5] == self.space[8]:
            print(f"{self.space[2]} gonna give it to ya!")
            quit()
        elif self.space[3] == self.space[6] == self.space[9]:
            print(f"{self.space[3]} gonna give it to ya!")
            quit()
        elif self.space[3] == self.space[5] == self.space[7]:
            print(f"{self.space[3]} gonna give it to ya!")
            quit()

    def all_spaces_filled(self):

        fill = all([space in ["X", "O"] for space in self.space.values()])
        if fill is True:
            print("Nothing else to do....  watch YouTube?")
            quit()
        else:
            pass


class TTT:
    def __init__(self):
        self.game_board = Board()
        p1name = input("Enter Your name Player1! ")
        self.p1 = Player(p1name, "X")
        print("Congrats you were assigned X!")
        p2name = input("Enter Your name Player1! ")
        self.p2 = Player(p2name, "O")
        print("Congrats you were assigned O!")
        self.turn = random.choice([self.p1, self.p2])

    def change_turn(self):
        if self.turn == self.p1:
            self.turn = self.p2
        else:
            self.turn = self.p1

    def play_game(self):
        while True:
            self.change_turn()
            print(f"Hey {self.turn.name} it's your turn!")
            while True:
                print(self.game_board)
                play_pos = int(
                    input(f"Where do you want to play an {self.turn.token}? ")
                )
                if self.game_board.play(play_pos, self.turn):
                    break
            self.game_board.check_winner()
            self.game_board.all_spaces_filled()


tic_tak_handgrenade = TTT()
tic_tak_handgrenade.play_game()
