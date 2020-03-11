
# 9 turns total
# first person gets 5
# second gets 4
# time limit between?
import random
import string
import time
#import brain
'''
Welcome Screen
Ask for players letter
Decide Who goes first
Show the board (current)
Get players Move
Check for Player Win
Check for Tie

Get computer's Move
Check if computer Won
Check for Tie

Play again?!
END
'''
#Welcome Screen
print("Welcome to the Tic Tac Toe Machine OF DEATH!!!!!!!")
#_________________________________________________________

possible_moves = ['00' ,'01', '02', '10', '11', '12', '20', '21', '22']
computer_moves = []
user_moves = []
total_number_of_moves = 0

def choose_letter(self): #this is a method
        if user_input_preference == 'X': #yup
            computer_input_preference = "O" #yup
            print("Xs it is! \n The computer will be Os")
            return user_input_preference #you cannot return 2 things! so...
            if user_input_preference == 'X': #we do this
                return computer_input_preference #and finally this
        else: 
            user_input_preference = 'O'         #yup
            computer_input_preference = "X"    #uh huh
            print("Os it is!")                 #maybe a little extra
            print("The computer will be Xs")   #okay this is extra
            return computer_input_preference    #again cannot return 2 things
            if computer_input_preference == "O": #whammy
                return user_input_preference       #and here we go!


def draw_board():    
    print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
    print("___|___|___")    
    print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
    print("___|___|___")    
    print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
    print("   |   |   ")    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' '] 

#ask for users letter choice

#Decide who goes first

def user_move1():
    user_first_move = input("Which spot would you like to move into?")
    user_moves.append(user_first_move)
    possible_moves.remove(f'{user_first_move}')
    print(f'Great! You have chosen {user_first_move}')
    if user_first_move == "00":
        board[1] = user_input_preference
    elif user_first_move == "10":
        board[2] = user_input_preference
    elif user_first_move == "20":
        board[3] = user_input_preference
    elif user_first_move == "01":
        board[4] = user_input_preference
    elif user_first_move == "11":
        board[5] = user_input_preference
    elif user_first_move == "21":
        board[6] = user_input_preference
    elif user_first_move == "02":
        board[7] = user_input_preference
    elif user_first_move == "12":
        board[8] = user_input_preference
    elif user_first_move == "22":
        board[9] = user_input_preference 
    
def user_move2():
    user_second_move = input("Which spot would you like to move into?")
    user_moves.append(user_second_move)
    possible_moves.remove(f'{user_second_move}')
    print(f'Great! You have chosen {user_second_move}')
    if user_second_move == "00":
        board[1] = user_input_preference
    elif user_second_move == "10":
        board[2] = user_input_preference
    elif user_second_move == "20":
        board[3] = user_input_preference
    elif user_second_move == "01":
        board[4] = user_input_preference
    elif user_second_move == "11":
        board[5] = user_input_preference
    elif user_second_move == "21":
        board[6] = user_input_preference
    elif user_second_move == "02":
        board[7] = user_input_preference
    elif user_second_move == "12":
        board[8] = user_input_preference
    elif user_second_move == "22":
        board[9] = user_input_preference
    
def user_move3():
    user_third_move = input("Which spot would you like to move into?")
    user_moves.append(user_third_move)
    possible_moves.remove(f'{user_third_move}')
    print(f'Great! You have chosen {user_third_move}')
    if user_third_move == "00":
        board[1] = user_input_preference
    elif user_third_move == "10":
        board[2] = user_input_preference
    elif user_third_move == "20":
        board[3] = user_input_preference
    elif user_third_move == "01":
        board[4] = user_input_preference
    elif user_third_move == "11":
        board[5] = user_input_preference
    elif user_third_move == "21":
        board[6] = user_input_preference
    elif user_third_move == "02":
        board[7] = user_input_preference
    elif user_third_move == "12":
        board[8] = user_input_preference
    elif user_third_move == "22":
        board[9] = user_input_preference 

def user_move4():
    user_forth_move = input("Which spot would you like to move into?")
    user_moves.append(user_forth_move)
    possible_moves.remove(f'{user_forth_move}')
    print(f'Great! You have chosen {user_forth_move}')
    if user_forth_move == "00":
        board[1] = user_input_preference
    elif user_forth_move == "10":
        board[2] = user_input_preference
    elif user_forth_move == "20":
        board[3] = user_input_preference
    elif user_forth_move == "01":
        board[4] = user_input_preference
    elif user_forth_move == "11":
        board[5] = user_input_preference
    elif user_forth_move == "21":
        board[6] = user_input_preference
    elif user_forth_move == "02":
        board[7] = user_input_preference
    elif user_forth_move == "12":
        board[8] = user_input_preference
    elif user_forth_move == "22":
        board[9] = user_input_preference

def user_move5():
    user_fifth_move = input("Which spot would you like to move into?")
    user_moves.append(user_fifth_move)
    possible_moves.remove(f'{user_fifth_move}')
    print(f'Great! You have chosen {user_fifth_move}')
    if user_fifth_move == "00":
        board[1] = user_input_preference
    elif user_fifth_move == "10":
        board[2] = user_input_preference
    elif user_fifth_move == "20":
        board[3] = user_input_preference
    elif user_fifth_move == "01":
        board[4] = user_input_preference
    elif user_fifth_move == "11":
        board[5] = user_input_preference
    elif user_fifth_move == "21":
        board[6] = user_input_preference
    elif user_fifth_move == "02":
        board[7] = user_input_preference
    elif user_fifth_move == "12":
        board[8] = user_input_preference
    elif user_fifth_move == "22":
        board[9] = user_input_preference

def comp_move1(computer_input_preference):
    computer_input_preference = computer_input_preference
    computer_first_move = random.choice(possible_moves)
    computer_moves.append(computer_first_move)
    possible_moves.remove(f'{computer_first_move}')
    print(f'Great! The computer has chosen {computer_first_move}')
    if computer_first_move == "00":
        board[1] = computer_input_preference
    elif computer_first_move == "10":
        board[2] = computer_input_preference
    elif computer_first_move == "20":
        board[3] = computer_input_preference
    elif computer_first_move == "01":
        board[4] = computer_input_preference
    elif computer_first_move == "11":
        board[5] = computer_input_preference
    elif computer_first_move == "21":
        board[6] = computer_input_preference
    elif computer_first_move == "02":
        board[7] = computer_input_preference
    elif computer_first_move == "12":
        board[8] = computer_input_preference
    elif computer_first_move == "22":
        board[9] = computer_input_preference 

def comp_move2():
    computer_second_move = random.choice(possible_moves)
    computer_moves.append(computer_second_move)
    possible_moves.remove(f'{computer_second_move}')
    print(f'Great! The computer has chosen {computer_second_move}')
    if computer_second_move == "00":
        board[1] = computer_input_preference
    elif computer_second_move == "10":
        board[2] = computer_input_preference
    elif computer_second_move == "20":
        board[3] = computer_input_preference
    elif computer_second_move == "01":
        board[4] = computer_input_preference
    elif computer_second_move == "11":
        board[5] = computer_input_preference
    elif computer_second_move == "21":
        board[6] = computer_input_preference
    elif computer_second_move == "02":
        board[7] = computer_input_preference
    elif computer_second_move == "12":
        board[8] = computer_input_preference
    elif computer_second_move == "22":
        board[9] = computer_input_preference 

def comp_move3():
    computer_third_move = random.choice(possible_moves)
    computer_moves.append(computer_third_move)
    possible_moves.remove(f'{computer_third_move}')
    print(f'Great! The computer has chosen {computer_third_move}')
    if computer_third_move == "00":
        board[1] = computer_input_preference
    elif computer_third_move == "10":
        board[2] = computer_input_preference
    elif computer_third_move == "20":
        board[3] = computer_input_preference
    elif computer_third_move == "01":
        board[4] = computer_input_preference
    elif computer_third_move == "11":
        board[5] = computer_input_preference
    elif computer_third_move == "21":
        board[6] = computer_input_preference
    elif computer_third_move == "02":
        board[7] = computer_input_preference
    elif computer_third_move == "12":
        board[8] = computer_input_preference
    elif computer_third_move == "22":
        board[9] = computer_input_preference 

def comp_move4():
    computer_forth_move = random.choice(possible_moves)
    computer_moves.append(computer_forth_move)
    possible_moves.remove(f'{computer_forth_move}')
    print(f'Great! The computer has chosen {computer_forth_move}')
    if computer_forth_move == "00":
        board[1] = computer_input_preference
    elif computer_forth_move == "10":
        board[2] = computer_input_preference
    elif computer_forth_move == "20":
        board[3] = computer_input_preference
    elif computer_forth_move == "01":
        board[4] = computer_input_preference
    elif computer_forth_move == "11":
        board[5] = computer_input_preference
    elif computer_forth_move == "21":
        board[6] = computer_input_preference
    elif computer_forth_move == "02":
        board[7] = computer_input_preference
    elif computer_forth_move == "12":
        board[8] = computer_input_preference
    elif computer_forth_move == "22":
        board[9] = computer_input_preference 

def comp_move5():
    computer_fifth_move = random.choice(possible_moves)
    computer_moves.append(computer_fifth_move)
    possible_moves.remove(f'{computer_fifth_move}')
    print(f'Great! The computer has chosen {computer_fifth_move}')
    if computer_fifth_move == "00":
        board[1] = computer_input_preference
    elif computer_fifth_move == "10":
        board[2] = computer_input_preference
    elif computer_fifth_move == "20":
        board[3] = computer_input_preference
    elif computer_fifth_move == "01":
        board[4] = computer_input_preference
    elif computer_fifth_move == "11":
        board[5] = computer_input_preference
    elif computer_fifth_move == "21":
        board[6] = computer_input_preference
    elif computer_fifth_move == "02":
        board[7] = computer_input_preference
    elif computer_fifth_move == "12":
        board[8] = computer_input_preference
    elif computer_fifth_move == "22":
        board[9] = computer_input_preference 

def updated_board():
    if '00' in possible_moves:
        pass
    elif '00' in user_moves:
        if user_input_preference == 'O':
            board[1] = O
        if user_input_preference == 'X':
            board[1] = X
    elif '00' in computer_moves:
        if user_input_preference == 'O':
            board[1] = X
        if user_input_preference == 'X':
            board[1] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    if '10' in possible_moves:
            pass
    elif '10' in user_moves:
        if user_input_preference == 'O':
                board[2] = O
        if user_input_preference == 'X':
                board[2] = X
    elif '10' in computer_moves:
        if user_input_preference == 'O':
                board[2] = X
        if user_input_preference == 'X':
                board[2] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    if '20' in possible_moves:
        pass
    elif '20' in user_moves:
        if user_input_preference == 'O':
            board[3] = O
        if user_input_preference == 'X':
            board[3] = X
    elif '20' in computer_moves:
        if user_input_preference == 'O':
            board[3] = X
        if user_input_preference == 'X':
            board[3] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    if '01' in possible_moves:
            pass
    elif '01' in user_moves:
        if user_input_preference == 'O':
            board[4] = O
        if user_input_preference == 'X':
            board[4] = X
    elif '01' in computer_moves:
        if user_input_preference == 'O':
            board[4] = X
        if user_input_preference == 'X':
            board[4] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    if '11' in possible_moves:
            pass
    elif '11' in user_moves:
        if user_input_preference == 'O':
                board[5] = O
        if user_input_preference == 'X':
                board[5] = X
    elif '11' in computer_moves:
        if user_input_preference == 'O':
                board[5] = X
        if user_input_preference == 'X':
                board[5] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    if '21' in possible_moves:
        pass
    elif '21' in user_moves:
        if user_input_preference == 'O':
            board[6] = O
        if user_input_preference == 'X':
            board[6] = X
    elif '21' in computer_moves:
        if user_input_preference == 'O':
            board[6] = X
        if user_input_preference == 'X':
            board[6] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    if '02' in possible_moves:
        pass
    elif '02' in user_moves:
        if user_input_preference == 'O':
            board[7] = O
        if user_input_preference == 'X':
            board[7] = X
    elif '02' in computer_moves:
        if user_input_preference == 'O':
            board[7] = X
        if user_input_preference == 'X':
            board[7] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    if '12' in possible_moves:
            pass
    elif '12' in user_moves:
        if user_input_preference == 'O':
            board[8] = O
        if user_input_preference == 'X':
            board[8] = X
    elif '12' in computer_moves:
        if user_input_preference == 'O':
            board[8] = X
        if user_input_preference == 'X':
            board[8] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    if '22' in possible_moves:
        pass
    elif '22' in user_moves:
        if user_input_preference == 'O':
            board[9] = O
        if user_input_preference == 'X':
            board[9] = X
    elif '22' in computer_moves:
        if user_input_preference == 'O':
            board[9] = X
        if user_input_preference == 'X':
            board[9] = O
        print(f"{board[1]}'|'{board[2]}'|'{board[3]}")    
        print("___|___|___")    
        print(f"{board[4]}'|'{board[5]}'|'{board[6]}")
        print("___|___|___")    
        print(f"{board[7]}'|'{board[8]}'|'{board[9]}") 
        print("   |   |   ")    
    else:
        print("How did we get here?")

user_input_preference()
total_number_of_moves = 0
starter = who_starts()

if starter == 'user': 
    while total_number_of_moves <9:
        total_number_of_moves = 0
        user_move1()
        total_number_of_moves += 1
        updated_board()
        #no winner yet
        comp_move1(computer_input_preference)
        total_number_of_moves += 1
        updated_board()
        #no winner yet
        user_move2()
        total_number_of_moves += 1
        updated_board()
        #no winner yet
        comp_move2()
        total_number_of_moves += 1
        updated_board()
        #no winner yet
        user_move3()
        total_number_of_moves += 1
        updated_board()
        #Check for winner here
        comp_move3()
        total_number_of_moves += 1
        update_board()
        #check for winner here
        user_move4()
        total_number_of_moves += 1
        updated_board()
        #Check for winner here
        comp_move4()
        total_number_of_moves += 1
        updated_board()
        #check for winner here
        user_move5()
        total_number_of_moves += 1
        updated_board()
        #Check for winner here
        ##GAME OVER or TIE AT THIS POINT FOR SURE
        user_move5()
        update_board()
        print("Tie Game!")
else:
    while total_number_of_moves <9:
        total_number_of_moves = 0
        comp_move1(computer_input_preference)
        total_number_of_moves += 1
        updated_board()
        user_move1()
        total_number_of_moves += 1
        updated_board()
        comp_move2()
        total_number_of_moves += 1
        updated_board()
        user_move2()
        total_number_of_moves += 1
        updated_board()
        #Check for winner here
        comp_move3()
        total_number_of_moves += 1
        updated_board()
        #check for winner here
        user_move3()
        total_number_of_moves += 1
        updated_board()
        #Check for winner here
        comp_move4()
        total_number_of_moves += 1
        updated_board()
        #check for winner here
        user_move4()
        total_number_of_moves += 1
        updated_board()
        #Check for winner here
        comp_move5()
        total_number_of_moves += 1
        updated_board()
        print("Tie Game!")
