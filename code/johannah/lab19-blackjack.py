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

three_cards = []
card_one = input("Enter first card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
card_two = input("Enter second card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
card_three = input("Enter third card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K): ")
# append card_one, card_two, & card_three into a list
three_cards.append(card_one)
three_cards.append(card_two)
three_cards.append(card_three)
print(three_cards)


# def my_func():
#     if card_one or card_two or card_three == 'A':
#         return 1
#     #elif card == 'J' or card == 'Q' or card == 'K':
#     elif card_one or card_two or card_three == 'J' or 'Q' or 'K':
#         return 10
#     #x = int(card_one + card_two + card_three)
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
sum_three = 0
for i in range(len(three_cards)):
    sum_three = sum_three + conversion[three_cards[i]]
print(sum_three)

#if sum < 17, advise to "Hit"
if sum_three < 17:
    print(f'{sum_three}, I advise you to \'Hit\'')
#elif sum >= 17 and sum < 21, advise to "Stay"
elif 17 <= sum_three < 21:
    print(f'{sum_three}, I advise you to \'Stay\'')
#elif sum == 21, advise "Blackjack!"
elif sum_three == 21:
    print(f'{sum_three} equals \'Blackjack!\'')
#elif sum > 21, advise "Already Busted"
else:
    print(f'{sum_three} equals \'Already Busted\'')
#Print out the current total point value and the advice