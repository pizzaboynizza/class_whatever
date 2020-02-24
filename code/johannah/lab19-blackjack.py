'''
Give basic blackjack playing advice during a game by asking the player for cards.

1. Ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)
2. Figure out the point value of each card individually. (Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1.)

Use the following rules to determine the advice:
-Less than 17, advise to "Hit"
-Greater than or equal to 17, but less than 21, advise to "Stay"
-Exactly 21, advise "Blackjack!"
-Over 21, advise "Already Busted"
-Print out the current total point value and the advice.
'''

three_cards = input("Enter three card choices (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
conversion = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
#add 3 numbers from user input
#if sum < 17, advise to "Hit"
#elif sum >= 17 and sum < 21, advise to "Stay"
#elif sum == 21, advise "Blackjack!"
#elif sum > 21, advise "Already Busted"
#Print out the current total point value and the advice