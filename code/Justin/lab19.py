def blackjack_advice(a, b, c):
    if a == "A":
        a = 1
    elif a == "Q":
        a = 10
    elif a == "J":
        a = 10
    elif a == "K":
        a = 10

    if b == "A":
        b = 1
    elif b == "Q":
        b = 10
    elif b == "J":
        b = 10
    elif b == "K":
        b = 10

    if c == "A":
        c = 1
    elif c == "Q":
        c = 10
    elif c == "J":
        c = 10
    elif c == "K":
        c = 10
    result = a + b + c
    print(result)

    if result < 17:
        print("Hit!")
    elif 17 <= result < 21:
        print("Stay")
    elif result == 21:
        print("Blackjack!")
    elif result > 21:
        print("Already busted")

blackjack_advice("Q","Q","Q")
