
class Player:

    def __init__(self,name,token):
        self.name = name
        self.token = token
   

class Game:
    def __init__(self):
        self.board = {
        '1,3':'1',
        '2,3':'2',
        '3,3':'3',
        '1,2':'4',
        '2,2':'5',
        '3,2':'6',
        '1,1':'7',
        '2,1':'8',
        '3,1':'9',}

    def __repr__(self):
        return f"{self.board['1,1']} | {self.board['2,1']} | {self.board['3,1']}\n{self.board['1,2']} | {self.board['2,2']} | {self.board['3,2']}\n{self.board['3,3']} | {self.board['2,3']}| {self.board['1,3']}"
        
        



    def move(self,x,y,player):
        # Do the rest of this
        if x == 1 and y == 1:
            self.board['1,1'] = player.token
        if x == 1 and y == 2:
            self.board['1,2'] = player.token
        if x == 1 and y == 3:
            self.board['1,3'] = player.token
        if x == 2 and y == 1:
            self.board['2,1'] = player.token
        if x == 2 and y == 2:
            self.board['2,2'] = player.token
        if x == 2 and y == 3:
            self.board['2,3'] = player.token
        if x == 3 and y == 3:
            self.board['3,3'] = player.token
        if x == 3 and y == 1:
            self.board['3,1'] = player.token
        if x == 3 and y == 2:
            self.board['3,2'] = player.token


    def calc_winner(self):
            if self.board['1,1'] == self.board['2,1'] ==  self.board['3,1']== 'X':
                print("Player X wins")     
            elif self.board['1,2'] == self.board['2,2'] ==  self.board['3,2']== 'X':
                print("Player X wins")   
            elif self.board['1,3'] == self.board['2,3'] ==  self.board['3,3']== 'X':
                print("Player X wins")   
            elif self.board['1,1'] == self.board['1,2'] ==  self.board['1,3']== 'X':
                print("Player X wins")   
            elif self.board['2,1'] == self.board['2,2'] ==  self.board['2,3']== 'X':
                print("Player X wins")   
            elif self.board['3,1'] == self.board['3,2'] ==  self.board['3,3']== 'X':
                print("Player X wins")   
            elif self.board['1,1'] == self.board['2,2'] ==  self.board['3,3']== 'X':
                print("Player X wins")   
            elif self.board['3,1'] == self.board['2,2'] ==  self.board['1,3']== 'X':
                print("Player X wins")   
            elif self.board['1,1'] == self.board['2,1'] ==  self.board['3,1']== 'O':
                print("Player O wins")     
            elif self.board['1,2'] == self.board['2,2'] ==  self.board['3,2']== 'O':
                print("Player O wins")   
            elif self.board['1,3'] == self.board['2,3'] ==  self.board['3,3']== 'O':
                print("Player O wins")   
            elif self.board['1,1'] == self.board['1,2'] ==  self.board['1,3']== 'O':
                print("Player O wins")   
            elif self.board['2,1'] == self.board['2,2'] ==  self.board['2,3']== 'O':
                print("Player O wins")   
            elif self.board['3,1'] == self.board['3,2'] ==  self.board['3,3']== 'O':
                print("Player O wins")   
            elif self.board['1,1'] == self.board['2,2'] ==  self.board['3,3']== 'O':
                print("Player O wins")   
            elif self.board['3,1'] == self.board['2,2'] ==  self.board['1,3']== 'O':
                print("Player O wins") 




    def is_full(self):
        for space in self.board:
            if self.board[space] in '1234567890':
                return False
        else:
            return True
        self.board
   
        


    def is_game_over(self):
        return self.is_full() or self.calc_winner()





playgame = Game()



player1 = Player(input("Player1 Name: "), 'X')
player2 = Player(input("Player2 Name: "), 'O')

token1 = 'X'
token2 = 'O'
counter = 0


while True:
    print("Welcome to Tic-Tac-Toe")
    if counter%2==0:
        current_player = player1
        counter +=1
        #.name pass the player name to class
        print(f"{player1.name}")
    elif counter%2==1:
        current_player = player2
        counter += 1
        print(f"{player2.name}")
    X = int(input("Where would you like to move X value?" ))
    Y = int(input("Where would you like to move Y value?" ))

    if player1.token == playgame.calc_winner():
        print(f"{player1.name}You win")
        break    
    elif player2.token == playgame.calc_winner():
        print(f"{player2.name}you win")
        break
    
    elif playgame.is_full():
        print("It is a Tie")
        break
    
    elif playgame.is_game_over():
        print("game is over")
        break


    playgame.move(X,Y, current_player)
    print(playgame)

