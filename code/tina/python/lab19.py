cardvalue = {
'A': 1,
'A1': 11,
'J': 10,
'K': 10,
'Q': 10,
'10': 10,
'9': 9,
'8': 8,
'7': 7,
'6': 6,
'5': 5,
'4': 4,
'3': 3,
'2': 2,
}

while True:
    print("If ACE is 10, Enter A1")
    card1 = input("Card one: ")
    card2 = input("Card Two: ")
    card3 = input("Card Three: ")

    value = (cardvalue[card1] + cardvalue[card2] + cardvalue[card3])
    



    if value <= 17:
        print(f"{value} Hit!")

    if value in range(17,21):
            print(f"Current card value: {value} Stay")
    if value == 21:
        print(f"Current card value: {value} Black Jack!")
    if value > 21:
        print(f"Current card value: {value} Already Busted!")

    user = input("New counters? ")
    if user not in ['yes','YES','y']:
        break

