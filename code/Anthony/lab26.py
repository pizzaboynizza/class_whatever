#1. player class 
#PROPERTIES 1: name = player name
#PROPERTY 2token = 'X' or 'O'
#2. Game class
#3. main function user REPL INPUT

class Player():
    def __init__(self, name, token): 
        self.name = name
        self.token = token
        

class Game():
    def __init__(self, board): 
        self.board = board
        board = ['_','_','_','_','_','_','_','_','_']
        

    def __repr__(self, board): #Returns a pretty string representation of the game board
        print(board[0] +'|' + board[1]+ '|'+ board[2])
        print(board[3] +'|' + board[4]+ '|'+ board[5])
        print(board[6] +'|' + board[7]+ '|'+ board[8])
        print(self.board)



    def move(self,player1,player)2:
        self.x = 
       
    def calc_winner(self, winner):
        self.winner = winner

    def is_full(self, full_game):
        for i in self.board:
            if 
        self.full_game = full_game


    def is_game_over(self, game_over):
        self.game_over = game_over
    

    # def main()



player1=Player(input)
player2= Player(input)
token1 = 'X'
token2 = 'O'
