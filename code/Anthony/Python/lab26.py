#board
# display board
# play game
# check win
# rows/columns/diadonals
# check tie

game_ongoing = True
winner = None
current_player = "X"

board = ["-","-","-", 
         "-","-", "-", 
         "-","-", "-"]


def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    show_board()
    while game_ongoing:
        player_move(current_player)
        check_game_over()
        change_player()
    if winner == "X" or winner == "O":
        print(winner + " won")
    elif winner == None:
        print("Tie")


def player_move(player):
    print(f"{player}'s turn")
    position = input("Choose a postion 1- 9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a postion 1- 9: ")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Position already taken, enter another position!")
    board[position] = player
    show_board()

def check_game_over():
    check_winner()
    check_tie()



def check_winner():
    global winner
    row_winner = check_row()
    column_winner = check_column()
    diagonal_winner = check_diagonal()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

def check_row():
    global game_ongoing
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[3] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # ANY WOR WITH A MATCH
    if row_1 or row_2 or row_3:
        game_ongoing = False

        # WINNER X OR O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_column():
    global game_ongoing
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    # ANY column WITH A MATCH
    if column_1 or column_2 or column_3:
        game_ongoing = False

        # WINNER X OR O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():
    global game_ongoing
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    
    
    # ANY WOR WITH A MATCH
    if diagonal_1 or diagonal_2:
        game_ongoing = False

        # WINNER X OR O
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return
def check_tie():
    global game_ongoing
    if "-" not in board:
        game_ongoing = False
    return


def change_player():
    global current_player
    # if current player was X, change to O
    if current_player == "X":
        current_player = "O"

    # if current player was O, change to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()

        

        



