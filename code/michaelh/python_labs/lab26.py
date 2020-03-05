'''
# Lab 26: Tic-Tac-Toe 

[Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) is a game.
Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid.
Whoever gets three in a row first wins.

You will write a **Player** class and **Game** class to model Tic Tac Toe, and a function **main** that models gameplay taking in user inputs through REPL.

The Player class has the following properties: 
* **name** = *player name*
* **token** = *'X' or 'O'*

The Game class has the following properties:
* **board** = *your representation of the board*

You can represent the board however you like, such as a 2D list, tuples, or dictionary.

The Game class has the following methods:
* `__repr__()` Returns a pretty string representation of the game board
```py
>>> print(board)
X| | 
O|X|O
 | | 
```

* `move(x, y, player)` Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.

```py
>>> board.move(2, 1, player_1)
 | | 
 | |X
 | | 
```

* `calc_winner()` What token character string has won or `None` if no one has.

```py
X| | 
O|X|O
 | |X
>>> board.calc_winner()
X
```

* `is_full()` Returns true if the game board is full.

```py
X|O|X
X|X|O
O|O|X
>>> board.is_full()
True
```

* `is_game_over()` Returns true if the game board is full or a player has won.

```py
X|O|X
X|X|O
O|O|X
>>> board.is_game_over()
True

X|O|
 | |X
 | |
>>> board.is_game_over()
False
```
'''
class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token
        if not (token == 'X' or token == 'O'):
            raise ValueError

class Game:
    def __init__(self):
        self.board = [['1','2','3'],['4','5','6'],['7','8','9']]

    def __repr__(self):
        repr_blanks = ''
        repr_digits = ''
        counter = 0
        for i in range(3):
            for j in range(3):
                counter += 1
                if self.board[i][j] == 'O' or self.board[i][j] == 'X':
                    repr_blanks += self.board[i][j]
                    repr_digits += '-'
                else:
                    repr_blanks += ' '
                    repr_digits += self.board[i][j]
                if j == 0 or j == 1:
                    repr_blanks += '|'
                    repr_digits += '|'
                else:
                    repr_blanks += '\n'
                    repr_digits += '\n'
        return repr_blanks+'\n'+'Valid moves:'+'\n'+repr_digits

    def move(self, x, y, player):
        if self.board[x][y] == 'X' or self.board[x][y] == 'O':
            raise ValueError
        self.board[x][y] = player.token

    def single_entry_move(self, entry, player):
        if not 0 < int(entry) < 10:
            raise ValueError
        self.move((int(entry)-1)//3, (int(entry)-1)%3, player)

    def calc_winner(self):
        for i in range(len(self.board)):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and (self.board[i][0] == 'X' or self.board[i][0] == 'O'):
                return self.board[i][0]
        for j in range(len(self.board[0])):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and (self.board[0][j] == 'X' or self.board[0][j] == 'O'):
                return self.board[0][j]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and (self.board[1][1] == 'X' or self.board[1][1] == 'O'):
            return self.board[1][1]
        if self.board[2][0] == self.board[1][1] == self.board[0][2] and (self.board[1][1] == 'X' or self.board[1][1] == 'O'):
            return self.board[1][1]

    def is_full(self):
        counter = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 'X' or self.board[i][j] == 'O':
                    counter += 1
        if counter == 9:
            return True
        else:
            return False

    def is_game_over(self):
        return self.is_full() or self.calc_winner() == 'X' or self.calc_winner() == 'O'

# g= Game()
# p1 = Player()
# print(g)
# print(g.calc_winner())
# print(g.is_full())
# print(g.is_game_over())
# g.move(0,0,p1)
# print(g)
# print(g.is_game_over())
# g.move(1,1,p1)
# print(g)
# print(g.is_game_over())
# g.move(2,2,p1)
# print(g)
# print(g.is_game_over())

def main():
    g = Game()
    p1_name = input('What is the first player\'s name? ')
    while True:
        p1_token = input(f'What is {p1_name}\'s token (\"X\" or \"O\")? ')
        try:
            p1 = Player(p1_name, p1_token)
            break
        except(ValueError):
            print('Try again!')
    p2_name = input('What is the second player\'s name? ')
    p2_token = 'X'
    if p1_token == 'X':
        p2_token = 'O' 
    p2 = Player(p2_name, p2_token)

    while not g.is_game_over():
        print(repr(g))
        while True:
            p1_move = input(f'What is {p1.name}\'s move? ')
            try:
                g.single_entry_move(p1_move, p1)
                break
            except (ValueError):
                print('Try again!')
        
        if g.is_game_over():
            break
        print(repr(g))

        while True:
            p2_move = input(f'What is {p2.name}\'s move? ')
            try:
                g.single_entry_move(p2_move, p2)
                break
            except (ValueError):
                print('Try again!')
    
    if g.calc_winner() == p1.token:
        print(f'{p1.name} is victorious!')
    elif g.calc_winner() == p2.token:
        print(f'{p2.name} is victorious!')
    else:
        print('Draw!')

main()