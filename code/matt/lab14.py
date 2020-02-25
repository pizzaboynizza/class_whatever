"""
Lab 14: Pick6
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'.
Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket 
and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and 
your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket 
numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, 
which can then be used for both the winning numbers and tickets. Another function could 
be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance

Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses.
Calculate your ROI, print it out along with your earnings and expenses.
"""
import random

# winner = []
# balance = 0
# ticket = []

# #generate winning ticket numbers
# while len(winner) < 6:
#     winner.append(random.randint(1, 100))
# print(winner)
def ticket():
    ticket = []
    while len(ticket) < 6:
        ticket.append(random.randint(1, 100))
    print(ticket)
    return ticket

# #generate user ticket
# while len(ticket) < 6:
#     ticket.append(random.randint(1, 100))
# print(ticket)
# 
# def ticket():
#     ticket = []
#     while len(ticket) < 6:
#         ticket.append(random.randint(1, 100))
#     print(ticket)
#     return ticket
# print(ticket)

#subtract ticket cost
# balance -= 2
#find how many numbers match
def matching_num():
    player1 = ticket()
    computer = ticket()
    count = 0
    balance = 0

    combined = zip(player1, computer)
    combined2 = list(combined)

    for x, y in combined2:
        if x == y:
            count += 1
    print(count)

    if count == 0:
        print(f"Losing ticket. Try again. Your current balance is ${balance}.")
    elif count == 1:
        balance += 4
        print(f"{count} matches. You win $4. Your current balance is ${balance}.")
    elif count == 2:
        balance += 7
        print(f"{count} matches. You win $7. Your current balance is ${balance}.")
    elif count == 3:
        balance += 100
        print(f"{count} matches. You win $100. Your current balance is ${balance}.")
    elif count == 4:
        balance += 50000
        print(f"{count} matches. You win $50,000. Your current balance is ${balance}.")
    elif count == 5:
        balance += 1000000
        print(f"{count} matches. You win $1,000,000. Your current balance is ${balance}.")
    elif count == 6:
        balance += 25000000
        print(f"{count} matches. You win $25,000,000. Your current balance is ${balance}.")
    


# winner()
# ticket()
matching_num()


# count = 0

# combined = zip(winner1, ticket1)
# combined2 = list(combined)
# print(combined2)

# for x, y in combined2:
#     if x == y:
#         count += 1
# print(count)
