# Lab 26
# Author : Joe

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

class Game:
    def __init__(self):
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def __repr__(self):
        return f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n--+---+--\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n--+---+--\n{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}\n"

    def move(self, x, y, player):
        if self.board[y][x] == " ":
            self.board[y][x] = player.token
            return True
        return False

    def calc_winner(self):
        # Check Horizontal
        for i in range(3):
            if self.board[i][0] != " " and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return self.board[i][0]
        # Check Vertical
        for i in range(3):
            if self.board[0][i] != " " and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return self.board[i][0]
        # Check Diagonal
        if self.board[0][0] != " " and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] != " " and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        # No Match
        return None

    def is_full(self):
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == " ":
                    return False
        return True

    def is_game_over(self):
        return self.is_full() or (self.calc_winner() != None)

    

print("Welcome to Tic-Tac-Toe!")
player1 = Player(input("Enter player one's name: "), "X")
player2 = Player(input("Enter player two's name: "), "O")
play_again = True

while play_again:
    game = Game()
    player_turn = True
    current_player = player1

    while not game.is_game_over():
        print(game)
        if player_turn:
            current_player = player1
        else:
            current_player = player2
        
        user_in = input(f"{current_player.name}, pick a spot (row col ; 0,0 is top left): ")
        user_in = user_in.split()
        if len(user_in) != 2:
            print("Invalid input!")
            continue
        try:
            y_pos = int(user_in[0])
            x_pos = int(user_in[1])
            if x_pos > 2 or x_pos < 0 or y_pos > 2 or y_pos < 0:
                print("Invalid input!")
                continue
        except ValueError:
            print("Invalid input!")
            continue

        if not game.move(x_pos, y_pos, current_player):
            print("Invalid input!")
            continue

        player_turn = not player_turn

    print(game)
    winner = game.calc_winner()
    if winner == None:
        print("Tie Game!")
    elif winner == player1.token:
        print(f"{player1.name} wins!")
    else:
        print(f"{player2.name} wins!")

    user_in = input("Play again? ").lower()
    while user_in == "" or (user_in[0] != "y" and user_in != "n"):
        user_in = input("Please enter yes or no: ")

    if user_in[0] == "y":
        play_again = True
    else:
        play_again = False



print("\nGoodbye!")

# print result