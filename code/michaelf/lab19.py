card_1 = input("pick a card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K): ")
card_2 = input("pick another card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K): ")
card_3 = input("pick another card (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K): ")

def blackjack(card_1, card_2, card_3):
    card_to_value = {'A': 1, '2': 2, '3' : 3, '4' : 4, '5': 5, '6': 6, '7' : 7, '8' : 8, '9': 9, '10': 10, 'J' : 10, 'Q': 10, 'K': 10}
    x = card_to_value[card_1]
    y = card_to_value[card_2]
    z = card_to_value[card_3]
    total = x + y + z 
    if total == 21:
        return str(total) + " Blackjack!"
    elif total < 17:
        return str(total) + " Hit"
    elif 16 < total < 21:
        return str(total) + " Stay"
    else:
        return str(total) + " Busted!"

print(blackjack(card_1, card_2, card_3))


