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

winning_ticket = []

for i in range(6):
    winning_ticket.append(random.randint(1,100))
print(f"The winning ticket is {winning_ticket}")


# Calculate Net Winnings 2. Start your balance at 0
earnings = [0, 4, 7, 100, 50000, 1000000, 25000000]
matches = 0
balance = 0
# loop thru lottery_ticket and match against winning_ticket AND loop thru matches and balance 100,100 times
times_played = 0

while times_played < 100000:  # TO TEST CHANGE TO < 100 or COMMENT OUT PRINT STATEMENT
    lottery_ticket = []
    times_played += 1
    balance -= 2
    for i in range(6):
        lottery_ticket.append(random.randint(1,100))
    print(lottery_ticket)


    if lottery_ticket[0] == winning_ticket[0]:
        matches += 1
        print(f"Yay! You have {matches} matches")
    elif lottery_ticket[1] == winning_ticket[1]:
        matches += 1
        print(f"Yay! You have {matches} matches")
    elif lottery_ticket[2] == winning_ticket[2]:
        matches += 1
        print(f"Yay! You have {matches} matches")
    elif lottery_ticket[3] == winning_ticket[3]:
        matches += 1
        print(f"Yay! You have {matches} matches")
    elif lottery_ticket[4] == winning_ticket[4]:
        matches += 1
        print(f"Yay! You have {matches} matches")
    elif lottery_ticket[5] == winning_ticket[5]:
        matches += 1
        print(f"Yay! You have {matches} matches")
    # DO I NEED TO LOOP THROUGH THIS 100,000 TIMES OR PUT IT IN THE WHILE OR FOR LOOP???
    else:
        print(f"You have {matches} matches")  # this should read "0 times" until there's at least 1 match in this loop
print(f"Alright! You have a total of {matches} matches")


if matches == 0:
    winnings = earnings[0]
    print(f"You earned ${winnings}")
    #you win $0
elif matches == 1:
    winnings = earnings[1]
    print(f"You earned ${winnings}")
    #you win $4
elif matches == 2:
    winnings = earnings[2]
    print(f"You earned ${winnings}")
    #you win $7
elif matches == 3:
    winnings = earnings[3]
    print(f"You earned ${winnings}")
    #you win $100
elif matches == 4:
    winnings = earnings[4]
    print(f"You earned ${winnings}")
    #you win $50,000
elif matches == 5:
    winnings = earnings[5]
    print(f"You earned ${winnings}")
    #you win $1,000,000
elif matches == 6:
    winnings = earnings[6]
    print(f"You earned ${winnings}")
    #you win $25,000,000
else:
    winnings = earnings[6]
    print(f"You have more than 6 matches! To be exact you have {matches} matches. You earned ${winnings}") #you win $25,000,000
print(f"You have won a total of ${winnings}")



#after 100,000 purchased tix at $2 each:
balance = winnings - 200000
print("Your expenses were $200,000 due to spending $2 per 100,000 lottery tickets.")
print(f"After 100,000 purchased lottery tickets, your balance/net winnings are ${balance}")
#ROI = (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
ROI = (balance / 200000)
print(f"Your ROI is ${ROI}")