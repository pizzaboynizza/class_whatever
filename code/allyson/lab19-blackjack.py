##  Let's Play Blackjack! ##

card= { 'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10 }

c1=input('First card?  ')
c2=input('Second card?  ')
c3=input('Third card?  ')

hand=(card[c1]+card[c2]+card[c3])

def card_check(hand):
    hand=(card[c1]+card[c2]+card[c3])
    if hand == 20:
        return("Stay") 
    if hand == 21:
        return("Blackjack!!")
    if hand >= 21:
        return('The Chips are down and the Buffalo is empty')    
    else:
        if hand < 17:
            return('Hit!')

print(card_check(hand))