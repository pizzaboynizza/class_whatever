"""
Lab 26: Tic-Tac-Toe
Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid.
Whoever gets three in a row first wins.

You will write a Player class and Game class to model Tic Tac Toe, and a function main that models 
gameplay taking in user inputs through REPL.

The Game class has the following properties:
board = your representation of the board

You can represent the board however you like, such as a 2D list, tuples, or dictionary.

The Game class has the following methods:
__repr__() Returns a pretty string representation of the game board
"""
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        self.row1 = ["1", "2", "3"]
        self.row2 = ["4", "5", "6"]
        self.row3 = ["7", "8", "9"]
        self.join1 = "|".join(self.row1)
        self.join2 = "|".join(self.row2)
        self.join3 = "|".join(self.row3)

    def move(self, x, y, player):
        # Place a player's token character string at a given coordinate (top-left is 0, 0),
        # x is horizontal position, y is vertical position.
        print(f"{self.join1}\n{self.join2}\n{self.join3}")
        player_num = input("Enter the position number you want to place your token in: ")

        for num in self.row1:
            if player_num == num:
                num = player.token
        for num in self.row2:
            if player_num == num:
                num = player.token
                # self.row2.replace(num, player.token)
        for num in self.row3:
            if player_num == num:
                num = player.token

    def calc_winner(self):
        if self.row1[0] == self.row1[1] == self.row1[2]:
            return self.row1[0]
        elif self.row2[0] == self.row2[1] == self.row2[2]:
            return self.row2[0]
        elif self.row3[0] == self.row3[1] == self.row3[2]:
            return self.row3[0]
        elif self.row1[0] == self.row2[0] == self.row3[0]:
            return self.row1[0]
        elif self.row1[1] == self.row2[1] == self.row3[1]:
            return self.row1[1]
        elif self.row1[2] == self.row2[2] == self.row3[2]:
            return self.row1[2]
        elif self.row1[0] == self.row2[1] == self.row3[2]:
            return self.row1[0]
        elif self.row1[2] == self.row2[1] == self.row3[0]:
            return self.row1[2]
    
    def is_full(self):
        for entry in self.row1:
            if entry in "0123456789":
                return False
        for entry in self.row2:
            if entry in "0123456789":
                return False
        for entry in self.row3:
            if entry in "0123456789":
                return False
        else:
            return True
    
    def is_game_over(self, is_full):
        #Returns true if the game board is full or a player has won.
        if is_full == True:
            print("Game board is full. It's a draw!")
        elif Game.calc_winner == True:
            print(f"{Game.calc_winner} wins!")
        else:
            print("Something went wrong. Error: is_game_over")
            return False

#setting players to their class and defining which token they'll use.
player1 = Player("Player 1", "X")
player2 = Player("Player 2", "O")
board = Game()

counter = 0
#counter for determining who's turn it is. Even numbers = player1 turn, odd = player2
if counter%2==0:
    board.move(1, 1, player1)
    counter += 1
elif counter%2==1:
    board.move(1, 1, player2)
    counter += 1

# while Game.is_game_over == False:
    # print(f"{join1}\n{join2}\n{join3}")
    # player_num = input("Enter the position number you want to place your token in: ")




# print(Game.is_full(1))

print(f"{board.join1}\n{board.join2}\n{board.join3}")
print(board.row1, board.row2, board.row3)