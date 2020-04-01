'''Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

Steps
Generate a list of 6 random numbers representing the winning tickets
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance'''
net_balance = 0

#will need a loop and conditional statements
#will need to import random for computer
import random
random.randint(0,99)
#make a variable to put random winnning numbers (0,99)

#will ask player(me) to select 6 numbers 0 -99
#make a variable for payoffs

#DEFINE A FUNCTION TO SELCT 6 RANDOM COMPUTER NUMBERS
def computer_numbers():
#NOT CANNOT SEARCH LIST LIKE THIS
   #for i in range(len(winning_numbers)):
    winning_numbers = []
#OR THIS 
   #for i in range(0,len(winning_numbers)6): 
    for i in range (0,6): #BECAUSE THE LIST IS STILL EMPTY??
        winning_numbers.append(random.randint(0,99))
    return winning_numbers
# print(computer_numbers()) #WHEN DO I NEED TO ADD A PARAMETER IN THE FUNCTION?



#DEFINE A FUNCTION THAT ENABLES YOU TO PICK 6 NUMBERS
def pick6_play():
#CREATE EMPTY AVARIABLE OUTSIDE THE LOOP TO APPEND ENTERD NUMBERS INTO
    pick6_numbers = []
    # while i == 0: WHY DID WHILE LOOP NOT WORK HERE?
    for i in range(0,6):
    #for i in range(0,6): CAN I LOOP?#CREAT A LOOP SO IT WILL ENTER NUMBERS IN A LOOP, OF AFTER ANOTHER AND NOT JUST MULTIPLE # AS 1 #
            mynumbers = int(input("Enter picked numbers 0-99: ")) #in the loop?
            pick6_numbers.append(mynumbers)
            # i+=1    #DONT NEED THIS?
    return pick6_numbers
# print(pick6_play())

pick6_numbers = pick6_play()
# # will ask the user to play 100,000 times
#DEFINE A FUNCTION TO TELL THE PLAYER TO PLAY 100,000 TIMES(LOOP)
# while i == 100000:
# #make a loop to calculate matches of mynumbers & winning numbers

# player_numbers = pick6_play()
# mixed_numbers = zip(random_numbers, player_numbers)
#mixed_numbers = set(mixed_numbers)
payoff_amount = 0
match = 0

i = 0

while i <=5: # or count<= 5
    match = 0 #will start from 0, and add when match achieved. will reset to 0 after going through whole loop
    payoff_amount-= 2
    random_numbers = computer_numbers()
    print(random_numbers, "this is rando")
    selected_numbers = pick6_numbers
    print(selected_numbers, "selected numbers")
    mixed_numbers = zip(random_numbers, selected_numbers)
    print(mixed_numbers)
    mixed_numbers = list(mixed_numbers)
    print(mixed_numbers)
    i+=1 #or count+=1
    for x,y in mixed_numbers: #x,y is nos in mixednumbers
        if x == y:
            match+=1
    else:
        pass
    if match == 1:
        payoff_amount+=2
    elif match == 2:
        payoff_amount += 7
    elif match == 3:
        payoff_amount+= 100
    elif match == 4:
        payoff_amount += 50000
    elif match == 5:
        payoff_amount+= 1000000
    elif match == 6:
        payoff_amount +=25000000
        
print(payoff_amount)











    # if  computer_numbers == player_numbers:
    #     match+=6
    #     playoff +=250000000
    




# #the loop will check the lenght of all 6 winning numbers
#     for i in range(1,len(winning_numbers)-1):

# #then make a conditional statement to compare the winning no vs mynumbers
#         if winning_numbers[1:-1] == my_numbers[1:-1]:
#             match =+6
#             payoff_amount ==25,000,000
#         elif winning_numbers[-1] > my_numbers[]:
#             match+=5
#             payoff_amount == 1,000,000
#         elif winning_numbers[-1] > my_numbers[]:
#             match =+6
#             payoff_amount ==25,000,000
#         elif winning_numbers[-1] > my_numbers[]:
#             match+=5
#             payoff_amount == 1,000,000
#         elif winning_numbers[-1] > my_numbers[]:
#             match+=5
#             payoff_amount == 1,000,000
#         elif winning_numbers[-1] > my_numbers[]:
#             match+=5
#             payoff_amount == 1,000,000
#         elif winning_numbers[-1] != my_numbers[i]:
#             match -=1
#             payoff_amount -=2



# to calculate net balance
# 6 random nos use import random and randint
#make random nos in a list

