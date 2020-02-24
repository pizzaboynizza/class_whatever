card_dictionary = {"A":1, "2":2,"3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

print("Choose the following options for cards: A, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q or K")
card_one = input('What\'s your first card? ' )
card_two = input('What\'s your second card? ')
card_three = input('What\'s your third card? ')

sum_of_cards = (card_dictionary[card_one] + card_dictionary[card_two] + card_dictionary[card_three])

def card_function(sum_of_cards):
    sum_of_cards = (card_dictionary[card_one] + card_dictionary[card_two] + card_dictionary[card_three])
    if sum_of_cards == 21:
        return("BlackJack!!")
    if sum_of_cards >= 22:
        return("You BUSTED!!")
    elif sum_of_cards <= 20:
        return("Stay!!")
    else:
        sum_of_cards <= 17
        return("Hit me!!")
print(card_function(sum_of_cards))