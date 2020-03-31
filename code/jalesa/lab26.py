# Lab 26: Tic-Tac-Toe
# Tic Tac Toe is a game. Players take turns placing tokens (a 'O' or 'X') into a 3x3 grid. Whoever gets three in a row first wins.

# You will write a Player class and Game class to model Tic Tac Toe, and a function main that models gameplay taking in user inputs through REPL.

# The Player class has the following properties:

# name = player name
# token = 'X' or 'O'
# The Game class has the following properties:

# board = your representation of the board
# You can represent the board however you like, such as a 2D list, tuples, or dictionary.

# The Game class has the following methods:

# __repr__() Returns a pretty string representation of the game board
# >>> print(board)
# X| | 
# O|X|O
#  | | 
# move(x, y, player) Place a player's token character string at a given coordinate (top-left is 0, 0), x is horizontal position, y is vertical position.
# >>> board.move(2, 1, player_1)
#  | | 
#  | |X
#  | | 
# calc_winner() What token character string has won or None if no one has.
# X| | 
# O|X|O
#  | |X
# >>> board.calc_winner()
# X
# is_full() Returns true if the game board is full.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_full()
# True
# is_game_over() Returns true if the game board is full or a player has won.
# X|O|X
# X|X|O
# O|O|X
# >>> board.is_game_over()
# True

# X|O|
#  | |X
#  | |
# >>> board.is_game_over()
# False


# board = [|,|]
# name = player_1

# class Player:
#     name = player_1
#     token = 'X' or 'O'
    




# class Game:
#     def __init__(self):


#     def __repr__(self,board):
#             print(board, board)

#     def move(x, y, player):
       


# user_input = REPL("")
# def game_play:

board = [' ' for x in range(10)]


def insert_letter(letter,pos):
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def print_board(board):
    print('   |    |')
    print(' ' + board[1] + ' | ' + board[2] +  '  | ' + board[3])
    print('   |    |')
    print('-----------')
    print('   |    |')
    print(' ' + board[4] + ' | ' + board[5]  + '  | ' + board[6])
    print('   |    |')
    print('-----------')
    print('   |    |')
    print(' ' + board[7] + ' | ' + board[8] +  '  | ' + board[9])
    print('   |    |')


def is_winner(board, letter):
    return (board[7] == letter and board[8] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[1] == letter and board[2] == letter and board[3] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter)


def player_move():
    run = True
    while run:
        move = input('Please select a position to place an \'x\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if space_is_free(move):
                    run = False
                    insert_letter('x', move)
                else: 
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')

        except:
            print('Please type a number!')




def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['o', 'x']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corner_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corner_open.append(i)

    if len(corner_open) > 0:
        move = select_random(corner_open)
        return move
    if 5 in possible_moves:
        move = 5
        return move


    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random(edges_open)

    return move




def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'o')):
            player_move()
            print_board(board)
        else:
            print('Sorry, o\'s won this time!')
            break

        if not(is_winner(board, 'x')):
            move = comp_move()
            if move == 0:
                print('Tie Game!')
            else:
                insert_letter('o', move)
                print('Computer place an \'o\' in position', move, ':')
                print_board(board)

        else:
            print('X\'s won this time! Good Job!')
            break


    if is_board_full(board):
        print('Tie Game!')

main()

# while True:
#     user_input = input('Play again?: ')
#     if user_input == "yes":
#         main()
       
