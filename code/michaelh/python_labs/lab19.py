'''
# Lab 19: Blackjack Advice


Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each cards individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

* Less than 17, advise to "Hit"
* Greater than or equal to 17, but less than 21, advise to "Stay"
* Exactly 21, advise "Blackjack!"
* Over 21, advise "Already Busted"

Print out the current total point value and the advice.

```
What's your first cards? Q
What's your second cards? 2
What's your third cards? 3
15 Hit

What's your first cards? K
What's your second cards? 5
What's your third cards? 5
20 Stay

What's your first cards? Q
What's your second cards? J
What's your third cards? A
21 Blackjack!
```

## Version 2 (optional)

Aces can be worth 11 if they won't put the total point value of both cardss over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
'''
cards = []
cards.append(input('What\'s your first card? '))
cards.append(input('What\'s your second card? '))
cards.append(input('What\'s your third card? '))
# print(cards)
num_cards = ['2','3','4','5','6','7','8','9','10']
# print(num_cards)

value = 0
aces = 0
for card in cards:
    if card == 'A':
        # value += 1
        aces += 1
    elif card in num_cards:
        value += int(card)
    else:
        value += 10

values = []
values.append(value)
if aces == 1:
    values[0] += 1
    values.append(value + 11)
elif aces == 2:
    values[0] += 2
    values.append(value + 12)
    # values.append(value + 22)
elif aces == 3:
    values[0] += 3
    values.append(value + 13)
    # values.append(value + 23)
    # values.append(value + 33)

if aces == 0:
    if value > 21:
        print(f'{value} bust.')
    elif value == 21:
        print(f'{value} blackjack.')
    elif value >= 17:
        print(f'{value} stay.')
    else:
        print(f'{value} hit.')
elif aces > 0:
    if max(values) > 21 and min(values) > 21:
        print(f'{min(values)} bust.')
    elif values[0] == 21 or values[1] == 21:
        print(f'21 blackjack.')
    elif max(values) > 21 and min(values) >= 17:
        print(f'{min(values)} stay.')
    else:
        print(f'{min(values)} hit.')
