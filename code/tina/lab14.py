"""
Version 2
The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses. 
"""
import random
# test to pull list out of list in list


# this is a def that will gen random numbers
def num():
    com6 = []
    while len(com6) < 6:
        com6.append(random.randint(1,100))
    return com6

balance = 0
#This is use my fu to pick a randoming winning number
winning = num()
print("this is winning", winning)
counter = 0
winning1 = 0

while counter < 100:
    #While loop will keep going till counter is == to the number set, counter inside of the loop will tell it how many to count each loop then stop
    ticket = num()
    counter += 1
    balance -=2
    # print( ticket)
    wip = zip(winning,ticket)
    wip1 = list(wip)
    print(wip1)
    for x,y in wip1:
        if x == y:
            winning1 += 1
           
 
    
print(winning1)    


if winning1 == 0:
    pass
elif winning1 == 1:
    balance += 4
elif winning1 == 2:
    balance += 7
elif winning1 == 3:
    balance += 100
elif winning1 == 4:
    balance += 50000
elif winning1 == 5:
    balance += 1000000
elif winning1 == 6:
    balance += 25000000



print(f" your current ${balance}")



roi = (balance - winning1)/balance

print("This is roi", roi)