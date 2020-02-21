# Lab 19 (version 2)
# Author : Joe

valid_cards = {"A" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6,
               "7" : 7, "8" : 8, "9" : 9, "10" : 10, "J" : 10, "Q" : 10, "K" : 10}

def getCard(msg):
    c = input(msg).upper()
    while c not in valid_cards:
        c = input("Not a valid card, please try again: ").upper()
    return c

cards = []
cards.append(getCard("Enter the first card: "))
cards.append(getCard("Enter the second card: "))
cards.append(getCard("Enter the third card: "))

total = [0]
aces = 0
for c in cards:
    total[0] += valid_cards[c]
    if c == "A":
        aces += 1

# 0 = 1, 1 = 2, 2 = 3, 3 = 4

for n in range(aces):
    total.append(total[n] + 10)

r_advice = ""
r_total = 0

print("Possible Options: ")
for t in total:
    if t < 17:
        advice = "Hit"
        #Only hit if no blackjack, no stay, and no lower value hit
        if (r_total < 17 or r_total > 21) and (r_total == 0 or r_total > t):
            r_total = t
            r_advice = advice
    elif t == 21:
        #Always recommend this
        advice = "Blackjack!!"
        r_advice = advice
        r_total = t
    elif t > 21:
        advice = "Already busted!"
        #Never recommend this unless it's the only option
        if r_total == 0:
            r_total = t
            r_advice = advice
    else:
        advice = "Stay"
        if r_total != 21:
            r_total = t
            r_advice = advice


    print(t, advice, sep="\t")

print("Recommended Option:")
print(f"{r_total}\t{r_advice}")