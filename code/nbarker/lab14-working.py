'''
Nick Barker
Lab 14
2/24/2020

Have the computer play pick6 many times and determine net balance.

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
After the loop, print the final balance
Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
'''
import random

def lottery_ticket_maker(int): #this function will make a lottery ticket (INTEGERS!)
    lottery_ticket = (random.sample(range(99), k=6)) #random sample of 6 numbers!
    print(lottery_ticket) #print that tickets
    return(lottery_ticket) #return the lotter_ticket values

def bought_ticket_maker(int): #this function will create a set of 6 random digits for the ticket to be refreshed over and over
    bought_ticket = (random.sample(range(99), k=6))
    print(bought_ticket) #print that puppy!
    return(bought_ticket) #return the bought_ticket value!

def comparison_tool(bought_ticket, lottery_ticket): #this function compares the two tickets and returns how much money was won (the $2 subtraction will be in the loop!)
    matches = 0 #gotta start at 0, starts over each loop!
    cash_money = [0, 4, 7, 100, 50000, 1000000, 25000000] #list of winnings
    for i in range(len(lottery_ticket)):   #for each item in the length of the lottery ticket
        if bought_ticket[i] == lottery_ticket[i]: #if there's a match
            matches += 1 #add a match to matches

    return cash_money[matches] #return how much cash_money was won 

print("Welcome to the pick-6-er!")

#generate a list of random numbers
input("Press Enter and the computer will randomly select 6 numbers!")
lottery_ticket = lottery_ticket_maker(int) #makes a list of ints to be lottery numbers
how_many_times = int(input("How many times would you like to play?"))

#PUT THIS IN THE LOOP!!!!
#bought_ticket_maker(int) #this is our one time use ticket numbers
#PUT THIS IN THE LOOP!!!!

balance = 0 #start at zero, FOR THE LOVE OF ALL THAT IS HOLY, KEEP THIS OUT OF THE LOOP1
q = 0  #how many times would you like to buy a new ticket and compare?
while q < how_many_times: #set the counter with how_many_times
    
    bought_ticket = bought_ticket_maker(int) #ints are ints are ints are ints
    balance -= 2 #$2 Dolla Ticket!
    take_home = comparison_tool(lottery_ticket, bought_ticket) #comparison tool gives us thea mount of money won(if any!)
    balance += take_home #add to balance based on winnings (minus ticket cost!)
    q += 1 #add to that counter!

print('Your final balance is:', balance) #this tells the user their balance
