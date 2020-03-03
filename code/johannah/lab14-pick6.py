'''
-Initially the program will pick 6 random numbers as the 'winner'.
-Then try playing pick6 100,000 times, with the ticket cost and payoff below
-A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff


Calculate your net winnings (the sum of all expenses and earnings):
-a ticket costs $2
-if 1 number matches, you win $4
-if 2 numbers match, you win $7
-if 3 numbers match, you win $100
-if 4 numbers match, you win $50,000
-if 5 numbers match, you win $1,000,000
-if 6 numbers match, you win $25,000,000

STEPS:
1. Generate a list of 6 random numbers representing the winning tickets
2. Start your balance at 0
3. Loop 100,000 times, for each loop:
4. Generate a list of 6 random numbers representing the ticket
5. Subtract 2 from your balance (you bought a ticket)
6. Find how many numbers match
7. Add to your balance the winnings from your matches
8. After the loop, print the final balance


-One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets.
-Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.
'''

import random

#def pick6():
winning_ticket = []

for i in range(6):
    #random_numbers = random.randint(1,100)
    winning_ticket.append(random.randint(1,100))
#return winning_ticket
print(f"The winning ticket is {winning_ticket}")
#pick6()

# Calculate Net Winnings 2. Start your balance at 0
# payout = [0, 4, 7, 100, 50000, 1000000, 25000000]
# net_winnings = payout - 2       # per ticket bought
net_winnings = [-2, 2, 5, 98, 49998, 999998, 24999998]  # each time use buy a ticket you lose $2

# MATCHING ticket numbers 100,000 TIMES
lottery_ticket = []
matches = 0
balance = 0

# loop thru lottery_ticket and match against winning_ticket AND loop thru matches and balance 100,100 times
times_played = 0

for i in range(6):
    # lottery_ticket.append(random.randint(1,100))
    # for x in range(100):  # each time use buy a ticket you lose $2
    #     balance = net_winnings
    # while times_played < 100001:
    while times_played < 21:
        times_played += 1
        lottery_ticket.append(random.randint(1,100))
print(f"Your lottery ticket numbers are {lottery_ticket}")

if lottery_ticket[i] == winning_ticket[i]:
    matches += 1
    print(f"Hey! You have {matches} matches")
else:
    print("Sorry, you have no matches")

if matches == 1:
    net_winnings = net_winnings[1]
    print(f"You earned ${net_winnings}")
    #you win $4
elif matches == 2:
    net_winnings = net_winnings[2]
    print(f"You earned ${net_winnings}")
    #you win $7
elif matches == 3:
    net_winnings = net_winnings[3]
    print(f"You earned ${net_winnings}")
    #you win $100
elif matches == 4:
    net_winnings = net_winnings[4]
    print(f"You earned ${net_winnings}")
    #you win $50,000
elif matches == 5:
    net_winnings = net_winnings[5]
    print(f"You earned ${net_winnings}")
    #you win $1,000,000
elif matches == 6:
    net_winnings = net_winnings[6]
    print(f"You earned ${net_winnings}")
    #you win $25,000,000
else:
    net_winnings = net_winnings[0]
    print(f"You earned ${net_winnings}")
    #you win $0
print(f"Net winnings: ${net_winnings}")



# 3. Loop 100,000 times, for each loop:
balance = 0

for i in range(100000):
    # ticket = winning_ticket
    # balance -= 2
    #lottery_ticket = lottery_ticket.append(random.randint(1,100))
    payout = net_winnings
    balance += net_winnings
    #print('100,000 tix', lottery_ticket.append(random.randint(1,100)))
print(f"After 100,000 purchased lottery tickets, your net winnings are ${balance}")


# lottery ticket random 6 numbers each time

# lottery_ticket = []
# i = 0
#for i in range(0,6):
    #lottery_ticket = []
# while i < 11:
#     i += 1
#     #print()
#     #randomNumbers = random.randint(1,100)
#     lottery_ticket.append(random.randint(1,100))
# print(lottery_ticket)