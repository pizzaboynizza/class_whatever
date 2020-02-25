"""
Lab 19: Blackjack Advice
Let's write a python program to give basic blackjack playing advice during a game by asking 
the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
Then, figure out the point value of each card individually. Number cards are worth their number, 
all face cards are worth 10. At this point, assume aces are worth 1. 
Use the following rules to determine the advice:

Version 2 (optional)
Aces can be worth 11 if they won't put the total point value of both cards over 21. 
Remember that you can have multiple aces in a hand. Try generating a list of all possible 
hand values by doubling the number of values in the output whenever you encounter an ace. 
For one half, add 1, for the other, add 11. 
This ensures if you have multiple aces that you account for the full range of possible values.
"""
Face_cards = {
    "A": 11,
    "J": 10,
    "Q": 10,
    "K": 10,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 11,
    "j": 10,
    "q": 10,
    "k": 10
}

user1 = input("What's your first card? ")
if user1 not in Face_cards:
    print("Must be a valid Playing Card")
    
user2 = input("What's your second card? ")
if user2 not in Face_cards:
    print("Must be a valid Playing Card")
    
user3 = input("What's your third card? ")
if user3 not in Face_cards:
    print("Must be a valid Playing Card")


card_value = Face_cards[user1] + Face_cards[user2] + Face_cards[user3]

num_ace = 0
for card in [user1, user2, user3]:
    if card == "a" or card == "A":
        num_ace += 1
        # print(num_ace)

if card_value > 21 and num_ace > 0:
    card_value = card_value - 10 * num_ace

if card_value == 21:
    print("21! Blackjack!")
elif card_value > 21:
    print(f"{card_value}. Already Busted")
elif card_value < 17:
    print(f"{card_value}. Hit.")
elif 17 <= card_value < 21:
    print(f"{card_value}. Stand.")