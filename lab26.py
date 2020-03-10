'''
Nick Barker
Lab26.py
'''
#I will continue to work on this one, I was so close, but was at 500 lines of code, yikes!


number_of_moves = 0
three_in_a_row = False
possible_moves = []
board = ['', ' ', ' ', ' ' ,' ' ,' ' ,' ' ,' ' ,' ' ,' ', ' ']
computer_moves = []
user_moves = []
class Game :
    #def __init__(self): #define the features with a constructor, What are the features of a game?

    def __repr__(board):                            #This prints the board that it gets passed!  Its looking to variables to fill the spaces on the board
        print('' + board[1] + '|' + board[2] + '|' + board[3])    
        print("___|___|___")    
        print('' + board[4] + '|' + board[5] + '|' + board[6])
        print("___|___|___")    
        print('' + board[7] + '|' + board[8] + '|' + board[9]) 
        print("   |   |   ")    
        board = [' ','XX ',' ',' ',' ',' ',' ',' ',' ',' '] 

    def makeMove(board, token, move):
        board[move] = letter

    def who_goes_first(): #defines who starts, based on random int between 0       and 1,this will return the value to 'who_goes_first,' this will determine if we start on user_move or computer_move
        if random.randint(0,1) == 0:
            return 'computer'
        else:
            return 'user'

    def name():
        user_name = input("Please enter your name, human!")
        return player_name
        
 
    def playAgain():
            # This function returns True if the player wants to play again, otherwise it returns False.
            print('Do you want to play again? (yes or no)')
            return input().lower().startswith('y')

    def getPlayerMove(board):
        #this is where we get the players move, we already know input preference and name from prior functions
        move = ''
        while move not in posssible_moves:
            print("Where would you like to move to?")
            move = input()
            user_moves.append(user_move)
            possible_moves.remove(f'user_move')
            print(f'Great! You have chosen {user_move}')
            return str(move)
    

    #def getComputerMove(board):
        
    
    #def user_move
    #def computer_move
        user_input_preference = user_input_preference
        computer_input_preference = computer_input_preference
        
    def who_starts():
        who_starts_digit = random.randint(0,1)
        if who_starts_digit == int(1):
            print("User will go first")
            return "user"
        else:
            print("Computer will go first")
            return "computer"

    def is_full():
        #This puppy checks the number of moves to see if the board is full, there cannot be more than 9 moves, so we can use this as an upper limit for board fullness, instead of checking each position individually
        if number_of_moves >= 9:
            print("Game Board is Full!") 
            return True  #if is_full is TRUE, this has got to trip 'game over'
        else:
            return False #if is_full is FALSE, no need to trip the 'gave over' function
    
    def is_game_over():
        if three_in_a_row is True:
            print("Game over!")
            if winner == 'player': 
                print("Great job player!")
            if winner == 'computer':
                print("The Machines have won!")    

    def isWinner(board, letter):
        # So we have a board, and we have letters (either X or O), if the same letter occupies the same 3 spots in a row, it will return TRUE if that player has won
        if (board[7] == letter and board[8] == letter and board[9] == letter): # across the top
            return three_in_a_row is True
        elif(board[4] == letter and board[5] == letter and board[6] == letter): # across the middle
            return three_in_a_row is True
        elif(board[1] == letter and board[2] == letter and board[3] == letter): # across the boardttom
            return three_in_a_row is True
        elif(board[7] == letter and board[4] == letter and board[1] == letter): # down the left side
            return three_in_a_row is True
        elif(board[8] == letter and board[5] == letter and board[2] == letter): # down the middle
            return three_in_a_row is True
        elif(board[9] == letter and board[6] == letter and board[3] == letter): # down the right side
            return three_in_a_row is True
        elif(board[7] == letter and board[5] == letter and board[3] == letter): # diagonal
            return three_in_a_row is True
        elif(board[9] == letter and board[5] == letter and board[1] == letter): # diagonal
            return three_in_a_row is True
        else:
            print("How did we get here?")

class Player:
    def __init__(self, name, token): #define the features of the player, name and token
        self.name = name
        self.token = token
    def __str__ (self):
        return (f"{self.name, {self.token}")

    