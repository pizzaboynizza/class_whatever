# Lab 27
# Author : Joe

red = "X"
black = "O"


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    
class Game:
    def __init__(self):
        self.board = []
        for i in range(6):
            self.board.append([" ", " ", " ", " ", " ", " ", " "])  #board[0] is topmost row

    def get_height(self, position):
        if position > 6 or position < 0:
            return -1
        for i in range(6):
            if self.board[i][position] != " ":
                return 6 - i
        return 0
    
    def move(self, player, position): # return False if move is illegal
        height = self.get_height(position)
        if height >= 6:
            print("That column is full!")
            return False
        elif height < 0:
            print("That is not a column!")
            return False
        else:
            self.board[5 - height][position] = player.color
            return True

    def calc_winner(self): #might require more testing
        # vertical
        for i in range(7):
            for k in range(3):
                if self.board[k][i] != " " and self.board[k][i] == self.board[k+1][i] and self.board[k+1][i] == self.board[k+2][i] and self.board[k+2][i] == self.board[k+3][i]:
                    return self.board[k][i]
        # horizontal
        for i in range(6):
            for k in range(4):
                if self.board[i][k] != " " and self.board[i][k] == self.board[i][k+1] and self.board[i][k+1] == self.board[i][k+2] and self.board[i][k+2] == self.board[i][k+3]:
                    return self.board[i][k]
        # diagonal up-right
        for i in range(4):
            for k in range(3):
                if self.board[k][i] != " " and self.board[k][i] == self.board[k+1][i+1] and self.board[k+1][i+1] == self.board[k+2][i+2] and self.board[k+2][i+2] == self.board[k+3][i+3]:
                    return self.board[k][i]
        # diagonal down-right
        for k in range(3):
            for i in range(5, 2, -1):
                if self.board[k][i] != " " and self.board[k][i] == self.board[k+1][i-1] and self.board[k+1][i-1] == self.board[k+2][i-2] and self.board[k+2][i-2] == self.board[k+3][i-3]:
                    return self.board[k][i]
        return None

    def is_full(self):
        for i in range(6):
            for k in range(7):
                if self.board[i][k] == " ":
                    return False
        return True

    def is_game_over(self):
        if self.is_full() or self.calc_winner() != None:
            return True
        return False

    def __str__(self):
        ret = ""
        for i in range(6):
            ret += f"{'+---'*7}+\n|"
            for k in range(7):
                ret += f" {self.board[i][k]} |"
            ret += "\n"
        ret += f"{'+---'*7}+\n"
        for i in range(7):
            ret += f"  {i} "
        ret += "\n"
        return ret


# Version 2
# game = Game()
# p1 = Player("1", red)
# p2 = Player("2", black)
# with open("../../1 Python/labs/connect_four/connect-four-moves.txt") as file:
#     turns = file.read().split("\n")

# turns[0] = 4 # there were some kind of junk characters on the first line, so this just manually replaces it with what's it's supposed to be

# player_turn = True
# for t in turns:
#     if player_turn:
#         current_player = p1
#     else:
#         current_player = p2
    
#     if game.move(current_player, int(t)-1):
#         player_turn = not player_turn

#     print(game)
# print(f"Winner is {game.calc_winner()}")


# Version 3
p1 = Player(input("Player 1, enter your name: "), red)
p2 = Player(input("Player 2, enter your name: "), black)

print(f"\n{p1.name}, you are {p1.color}\n{p2.name}, you are {p2.color}\n")

play_again = True

while play_again:
    game = Game()
    player_turn = True
    while not game.is_game_over():
        print(game)
        if player_turn:
            current_player = p1
        else:
            current_player = p2
        
        pos = input(f"{current_player.name}, enter column to place piece: ")
        try:
            pos = int(pos)
            if game.move(current_player, pos):
                player_turn = not player_turn
        except ValueError:
            print("Must enter a number!")

    print(game)
    winner = game.calc_winner()
    if winner == None:
        print("Tie game!")
    elif winner == red:
        print(f"{p1.name} wins!")
    else:
        print(f"{p2.name} wins!")
    
    user_in = input("Play again? ").lower()
    while user_in == "" or (user_in[0] != "y" and user_in != "n"):
        user_in = input("Please enter yes or no: ")

    if user_in[0] == "y":
        play_again = True
    else:
        play_again = False