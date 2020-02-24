'''
Nick Barker
Lab 19
2/21/2020
'''

'''
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.
'''
#I misread the question, and made all values different, K=13, Q=12, J=11, uggghhhhh
#I realize my functions could be much more simple, but to save time I changed the values 11, 12, 13 all to == 10

card1 = input("Please enter your first card, choose from A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K, and please hit <enter> between cards!")

card1 = card1.upper()

print(f"Your first card is {card1}")

card2 = input("Please enter your next card")
card2 = card2.upper()

print(f"So far, you have {card1}, and {card2}")
card3 = input("Please enter your last card")
card3 = card3.upper()

print(f"Your cards are {card1}, {card2}, and {card3}")
correct = input("Is this correct?")

if correct == "yes":
    print("Great!")
else: 
    print("Let's start over!")
    print("Goodbye!")

#user input is good to go!
#converts strings to uppercase
#converts uppercase to ints
#leaves ints as ints


#I know that writing 3 functions that are VERY similar defeats the purpose of writing a function, but this is what worked for me...

def numbamaker(card):
    if card1 == "A":
        print("card value is 1")
        return(int(1))
    if card1 == "J":
        print("card value is 11")
        return(int(10))
    if card1 == "K":
        print("card value is 13")
        return(int(10))
    if card1 == "Q":
        print("card value is 12")
        return(int(10))
    else:
        z = int(f"{card1}")
        return int(z)

def numbamaker2(card):
    if card2 == "A":
        print("card value is 1")
        return(int(1))
    if card2 == "J":
        print("card value is 11")
        return(int(10))
    if card2 == "K":
        print("card value is 13")
        return(int(10))
    if card2 == "Q":
        print("card value is 12")
        return(int(10))
    else:
        z = int(f"{card2}")
        return int(z)

def numbamaker3(card):
    if card3 == "A":
        print("card value is 1")
        return(int(1))
    if card3 == "J":
        print("card value is 11")
        return(int(10))
    if card3 == "K":
        print("card value is 13")
        return(int(10))
    if card3 == "Q":
        print("card value is 12")
        return(int(10))
    else:
        zzz = int(f"{card3}") 
        return int(zzz)

card1_total = numbamaker(card1)
card2_total = numbamaker2(card2)
card3_total = numbamaker3(card3)

print(card1_total)
print(card2_total)
print(card3_total)

num_total = card1_total + card2_total + card3_total

print(f"Your current card value is {num_total}")

if num_total == 21:
    print("BLACKJACK MOTHERF******S!!!!")
    print("It is recommended that you stay")
elif num_total < 17: 
    print("Based on your current cards, it is advised that you HIT")
elif 17 <= num_total < 21:
    print("Based on your current cards, it is advised that you STAY")
else:
    print("ALREADY BUSTED!")