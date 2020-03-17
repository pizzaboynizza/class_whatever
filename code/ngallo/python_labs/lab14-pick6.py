import random

# set list of lottery numbers to compare to:'
def random_gen():
    return[random.randrange(1,100) for i in range (6)]
random_gen()

lottery_numbers = random_gen()

def lottery_function(lottery_numbers):
    q = 0
    user_balance = 0
    while q < 10000: #change to 100,000 to complete lab
        
        user_ticket = [random.randrange(1,100) for i in range (6)]
        user_balance -= 2
        zipped_ticker = 0

        print("This is your ticket: ", user_ticket)
        print("These are the winning numbers.", lottery_numbers)
        print("Your current balance.", user_balance) 

        zipped = zip(user_ticket, lottery_numbers)
        zipped_list = list(zipped)

        for x,y in zipped_list:
            if x == y:
                zipped_ticker += 1
            else:
                pass

        if zipped_ticker == 1:
            user_balance += 4
            print("You won 4 dollars")
        elif zipped_ticker == 2:
            user_balance += 7
            print("You won 7 dollars")
        elif zipped_ticker == 3:
            user_balance += 100
            print("You won 100 dollars")
        elif zipped_ticker == 4:
            user_balance += 50000
            print("You won 50000 dollars")
        elif zipped_ticker == 5:
            user_balance += 1000000
            print("You won 1000000 dollars")
        elif zipped_ticker == 6:
            user_balance += 25000000
            print("You won 25000000 dollars")
        else:
            user_balance += 0
            print("2 dollars to play again")
        q += 1
    else:
        print("100,000 tickets have been anyalized!")

    print("you won", zipped_ticker, "times.")

lottery_function(lottery_numbers)





# Lab 14: Pick6
# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

# Steps
# Generate a list of 6 random numbers representing the winning tickets
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance
# Version 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.