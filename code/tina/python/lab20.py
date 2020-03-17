
while True:

    card = input("Enter a card number: ")
    # spilt a input list, make it so pop will pop out a number
    # list() put it in to list, map() put inside of list and card is the variabel to use. 
    card = list(map(int, card))

    # store number else where for use later
    g = card.pop(-1)

    # changing order of numbers in list
    card.reverse()

    # i is index for enumerate %(moudles is every 2 number) else do nothing with index. enmuetare is giving index to card
    double = [x * 2 if i%2==0 else x for i, x in enumerate(card)]

    # If number is great then 9 subtrack it - else leave it alone 
    nine = [n - 9 if n > 9 else n for n in double]

    a = sum(nine)
    print(a)

    print(g)

    user = input("Check another credit card number? ")
    if user not in ["yes","y","Yes"]:
        break













