# Lab 19: Blackjack Advice
# Let's write a python program to give basic 
# blackjack playing advice during a game by asking 
# the player for cards. First, ask the user for
#  three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K).
#  Then, figure out the point value of each card individually.
#  Number cards are worth their number, all face cards are worth 10.
#  At this point, assume aces are worth 1. Use the following 

# how do i make my input access my dictionairies

def blackjack():
    first_card = input('Enter your first card: ')
    second_card = input("Enter your second card: ")
    third_card = input("Enter your third card: ")
    collection = {
    "a": 1,
    "2": 2,
    "3": 3,
    "4" : 4,
    "5" : 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10":10,
    "j" : 10,
    "q" : 10,
    "k" : 10,
    }
    total = (collection[first_card] + collection[second_card] + collection[third_card])
    print(total)

    if total < 17:
        print("HIT")
    if 17 <= total < 21:
        print("STAY")
    if total == 21:
        print("BLACKJACK!")
    if total > 21:
        print("ALREADY BUSTED")


while True:
    print("WELCOME TO BLACKJACK")
    keep_going = input("would you like to continue yes or no? ") 
    if keep_going == "yes":
        blackjack()
        continue

    else:
         break
# 
# # rules to determine the advice:
# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.

# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!

# Version 2 (optional)
# Aces can be worth 11 if they won't put the total point
#  value of both cards over 21. Remember that you can
#  have multiple aces in a hand. Try generating a list
#  of all possible hand values by doubling the number
#  of values in the output whenever you encounter an ace.
#  For one half, add 1, for the other, add 11. This ensures
#  if you have multiple aces that you account for the full
#  range of possible values.

# if total >= 21:
#     "a" == 11




