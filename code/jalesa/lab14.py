'''Lab 14: Pick6
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'.
 Then try playing pick6 100,000 times, with the ticket cost 
 and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of 
matches between the ticket and the winning numbers 
determines the payoff. Order matters, if the winning
 numbers are [5, 10] and your ticket numbers are [10, 5]
you have 0 matches. If the winning numbers are [5, 10, 2]
and your ticket numbers are [10, 5, 2], you have 1 match.
Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will
 generate a list of 6 random numbers, 
 which can then be used for both the winning 
 numbers and tickets. Another function could 
 be num_matches(winning, ticket) which returns
  the number of matches between the winning numbers and the ticket.

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
The ROI (return on investment) is defined as 
(earnings - expenses)/expenses. Calculate your 
ROI, print it out along with your earnings and expenses.'''

import random
winning_ticket = []


# random.sample(range(1, 50), 7) makes a list of 7 random numbers
# starting at 1 and ending with 49.
# the result of return random.sample(range(1,100),6)  saves into the function pick6()
def pick6():
    return random.sample(range(1,100),6) 


# saving the function into a variable so that i can reuse it.
winning_ticket = pick6()

# balance and count has to be defined outside of the loop to manipulate
# it in the loop.
# create while loop to do something 1,000 times
# save pick6() in ticket because...
# winning_ticket is defined outside the loop because it is the computer generated numbers,and ticket inside the loop is giving me a new ticket 
# 100,000 times. winning ticket has to be defined outside the loop because you dont want a different ticket everytime we go through the loop.
# zip(winning_ticket, ticket) returns a zip object. The first and second element of each variable pairs together and creates a tuple. Must save in a new variable and turn it into a list so that it is readable. Match = 0 is in the while loop and not outside the loop because you want to check if each tuple are matches. Not check every time the ticket is a winner.

count = 0
balance = 0
while count < 10:
    ticket = pick6()
    print(ticket)
    new = zip(winning_ticket, ticket)
    new2 = list(new)
    print("tuple of winning_ticket and ticket",new2)
    count += 1
    match = 0
    balance -= 2
    
    # use for x,y because i am using a tuple
    for x,y in new2:
        if x == y:
            match += 1
            # to buy the ticket it cost $2.00 and you win $4.00 with 1 match
    if match == 2:
        balance += 4
    elif match == 3:
        match += 1
        balance += 100
    elif match == 4:
        match += 1
        balance == 50000
    elif match == 5:
        match += 1
        balance == 1000000
    elif match == 6:
        balance == 25000000 
            
    print("your matches are", match)
print("your balance is", balance)

        








   