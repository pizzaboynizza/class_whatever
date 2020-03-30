# write a python program to give basic blackjack playing advice during a game by asking the player for cards.

def blackjack_game():# define function

    cards = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'10':10, 'J':10, 'K':10, 'Q':10}
    card_no1 = input("Enter card 1: ")
    card_no2 = input("Enter card 2: ")
    card_no3 = input("Enter card 3: ")
    # letters = ["J", "K", "Q", "K"]
    # numbers = [2,3,4,5,6,7,8,9,10]
    # a = []
    
    total_cards = (cards[card_no1] + cards[card_no2] + cards[card_no3])
    print(total_cards)

    # if cards == a:
    #     return 1
    # elif cards == letters:
    #     return 10
    # elif cards == numbers:
    #     return 
    

    if total_cards < 17:
        return ("hit..")
    elif total_cards >= 17 and total_cards < 24:
        return ("Stay")
    elif total_cards == 21:
        return  ("Blackjack")
    else:
        return ("Already Busted")
print(blackjack_game())
    
# A = 1    # Assign card values
# J = 10
# Q = 10
# K = 10
# 2 = 2
# 3 = 3
# 4 = 4
# 6 = 6
# 7 = 7
# 9  = 9
# 10 = 10

#     user_input = input("Enter 3 playing cards: ") #user inputs 3 cards
#     if user_input == number
   
