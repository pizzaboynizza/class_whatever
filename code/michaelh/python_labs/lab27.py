'''
# Lab 27: Connect Four

[Connect Four](https://en.wikipedia.org/wiki/Connect_Four) is a board game.
Players take turns placing tokens of their color into a vertical grid.
They drop to the bottom, and if anyone has four of their color in a straight line, they've won!

Define a module that simulates a Connect Four game.

This will consist of the following classes:

`Player`:
- Properties
    - `name`
    - `color`
        
`Game`:
- Properties
    - `board`: 7x6 board representation

- Methods
    - `get_height(position)`: returns int of how many pieces occupy a column 
    - `move(player, position)`: adds a player token to a column after figuring out the current height of the column 
    - `calc_winner()`: returns true if a match (four in a row) is found 
    - `is_full()`: returns true if all board positions are occupied 
    - `is_game_over()`: returns true if the game is over (a winner is found or the board is full)


Create a program that simulates the _just playing moves_ of an existing Connect Four game.
Do not concern yourself with figuring out who has won.

It will read a file that contains a history of the moves in a game.
Assume the playing board is made of columns numbered 1 through 7.
The file will have one line for each move (players alternate).
The number in that line is the column the current player placed a token in.

Use the following [example move file](./connect_four/connect-four-moves.txt).
Save it in something like `connect-four-moves.txt`
This moves file recreates [this game](https://en.wikipedia.org/wiki/File:Connect_Four.gif).

*   Think about how to figure out how far that token will fall in a given column.

*   Think about how to place a token in a column.

*   Think about how to concisely store the tokens that have been dropped in the board.

*   Read in moves from the file.

*   After each move, print out a representation of the board.
    You can use `R` and `Y` to represent the pieces.

## Version 2

*   Once all moves are done, also print out what player, if any, won.

## Version 3

*   Make game playable
'''
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        if not (color == 'R' or color == 'Y'):
            raise ValueError('That is not a valid color. ')

class Game:
    def __init__(self):
        col = 7
        row = 6 
        self.board = []
        for i in range(col):
            new_row = []
            for j in range(row):
                new_row.append(' ')
            self.board.append(new_row)


    def __str__(self):
        str_repr = '1 2 3 4 5 6 7\n'
        for i in range(7):
            height = self.get_height(i)
            if height == 6:
                print(str_repr.count(str(i+1)))
                str_repr = str_repr.replace(str(i+1), '-')

        for i in range(-1, -1 - len(self.board[0]), -1):
            for j in range(len(self.board)):
                str_repr += str(self.board[j][i])
                if j == (len(self.board) - 1):
                    str_repr += '\n'
                else:
                    str_repr += '|'
        return str_repr


# returns int of how many pieces occupy a column 
    def get_height(self, position):
        col = self.board[position]
        height = 0
        while col[height] != ' ':
            height += 1
            if height == 6:
                break
        return height
            

# adds a player token to a column after figuring out the current height of the column 
    def move(self, player, position):
        height = self.get_height(position)
        # print(height)
        if not (0 <= position <=7) or height > 5:
            raise ValueError('That is not a valid move. ')
        # print(position, height)
        self.board[position][height] = player.color

# returns true if a match (four in a row) is found
    def calc_winner(self):
        directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != ' ':
                    for d in directions:
                        if self.__winner_dir(i, j, d[0], d[1]):
                            return self.board[i][j]
        return ' '

# used for looping through each direction and 
    def __winner_dir(self, x0, y0, dx, dy):
        token =  self.board[x0][y0]    
        for i in range(1,4):
            if not (0 <= x0 + dx * i < len(self.board)) or not (0 <= y0 + dy * i < len(self.board[0])):
                return False
            elif self.board[x0 + dx * i][y0 + dy * i] != token:
                return False
        return True

# returns true if all board positions are occupied
    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == ' ':
                    return False
        return True

# returns true if the game is over (a winner is found or the board is full)
    def is_game_over(self):
        return (self.calc_winner() != ' ') or self.is_full()

p1_name = input('What is the first player\'s name? ')
while True:
    p1_color = input(f'What is {p1_name}\'s color (\"R\" or \"Y\")? ')
    try:
        p1 = Player(p1_name, p1_color)
        break
    except(ValueError) as e:
        print(e, 'Try again!')  
p2_name = input('What is the second player\'s name? ')
p2_color = 'R'
if p1_color == 'R':
    p2_color = 'Y' 
p2 = Player(p2_name, p2_color)

g = Game()
# print(g.is_game_over())
# print(g.is_full())
# print(g.calc_winner())
while not g.is_game_over():
    print(g)
    while True:
        p1_move = input(f'What is {p1.name}\'s move? ')
        try:
            g.move(p1, int(p1_move)-1)
            break
        except (ValueError, TypeError, IndexError) as e:
            print(e, 'Try again!')
    if g.is_game_over():
        break

    print(g)
    while True:
        p2_move = input(f'What is {p2.name}\'s move? ')
        try:
            g.move(p2, int(p2_move)-1)
            break
        except (ValueError, TypeError, IndexError) as e:
            print(e, 'Try again!')

if g.calc_winner() == p1.color:
    print(g)
    print(f'{p1.name} is victorious!')
elif g.calc_winner() == p2.color:
    print(g)
    print(f'{p2.name} is victorious!')
elif g.is_full():
    print(g)
    print('Draw!')
else:
    print('Something has gone horribly wrong. Draw!')
# filename = 'connect-four-moves.txt'
# with open('/home/michael/Desktop/'+filename, 'r') as f:
#     contents = f.read().lower()
# moves = contents.split('\n')
# p1 = Player('Player 1', 'R')
# p2 = Player('Player 2', 'Y')
# g = Game()
# print(moves)
# print(g)
# for turn_num in range(len(moves)//2):
#     g.move(p1, int(moves[turn_num*2])-1)
#     if g.calc_winner() == 'R':
#         print('Player 1 is victorious!')
#         print(g)
#         break
#     elif g.calc_winner() == 'Y':
#         print('Player 2 is victorious!')
#         print(g)
#         break
#     g.move(p2, int(moves[turn_num*2+1])-1)
#     if g.calc_winner() == 'R':
#         print('Player 1 is victorious!')
#         print(g)
#         break
#     elif g.calc_winner() == 'Y':
#         print('Player 2 is victorious!')
#         print(g)
#         break
#     print(g)