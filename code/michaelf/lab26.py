class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
    def __str__(self):
        return f"{self.name}, {self.token}"

class Game:
    def __init__(self):
        self.board = {'0,0': ' ', '0,1': ' ', '0,2': ' ', '1,0': ' ', '1,1': ' ', '1,2': ' ', '2,0': ' ', '2,1': ' ', '2,2': ' '}
    def __repr__(self):
        self.board_pr = f"  0 1 2\n0 {self.board['0,0']}|{self.board['1,0']}|{self.board['2,0']}\n1 {self.board['0,1']}|{self.board['1,1']}|{self.board['2,1']}\n2 {self.board['0,2']}|{self.board['1,2']}|{self.board['2,2']}"
        return self.board_pr
    def move(self, x, y, player):
        coord = f'{x},{y}'
        self.board[coord] = f'{player.token}'

    def calc_winner(self):
        if self.board['0,0'] != ' ' and self.board['0,0'] == self.board['0,1'] == self.board['0,2']:
            return True
        elif self.board['0,0'] != ' ' and self.board['0,0'] == self.board['1,0'] == self.board['2,0']:
            return True
        elif self.board['0,0'] != ' ' and self.board['0,0'] == self.board['1,1'] == self.board['2,2']:
            return True
        elif self.board['1,0'] != ' ' and self.board['1,0'] == self.board['1,1'] == self.board['1,2']:
            return True
        elif self.board['2,0'] != ' ' and self.board['2,0'] == self.board['2,1'] == self.board['2,2']:
            return True
        elif self.board['0,2'] != ' ' and self.board['0,2'] == self.board['1,1'] == self.board['2,0']:
            return True
        elif self.board['0,1'] != ' ' and self.board['0,1'] == self.board['1,1'] == self.board['2,1']:
            return True
        elif self.board['0,2'] != ' ' and self.board['0,2'] == self.board['1,2'] == self.board['2,2']:
            return True
        else:
            return False
    def is_full(self):
        if ' ' not in list(self.board.values()):
            return True
        else:
            return False
    def is_game_over(self):
        if self.calc_winner() == True:
            return True
        elif self.is_full() == True:
            return True
        else:
            return False

def main():
    tictac = Game()
    print(tictac.__repr__())
    name = input("Player One Name: ")
    token = input("Player One Choose token (X or O): ").upper()
    player1 = Player(name, token)
    name = input("Player Two Name: ")
    token = input("Player Two choose token (X or O): ").upper()
    player2 = Player(name, token)    
    while tictac.is_game_over() == False:

        which_player = input(f"Whose turn? 1.{player1.name} or 2.{player2.name}: ")
        if which_player == '1':
            player = player1
        elif which_player == '2':
            player = player2
        x = input("x coordinate between 0 and 2: ")
        y = input("y coordinate between 0 and 2: ")
        tictac.move(x,y,player)
        print(tictac.__repr__())
        if tictac.calc_winner() == True:
            print(f"{player.name} wins!!!")
        if tictac.is_full() == True:
            print("Cat's game!")

main()