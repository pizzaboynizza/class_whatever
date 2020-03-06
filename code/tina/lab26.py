class player:

    def __init__(self):
        pass


    def move(self):
        pass
        # self.playername = input("What is your name? ")
        # self.token = {1:'x',2:'o'}
        # self.move = input()



class game:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = {1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',}
        


    def __repr__(self):
        #Give back the point it has been given. 
        pass


    def gameboard(self,board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])


    def move(self,player):
        self.x
        self.y
        pass


    def calc_winnter(self):
        pass


    def is_full(self):
        pass


    def is_game_over(self):
        pass