##  Lottery!!  ##
import random


def lot():
    tix = []
    for i in range(6):
        tix.append(random.randint(1, 99))
    return tix


def pay(tix, win):
    num_match = 0
    for i in range(6):
        if tix[i] == win[i]:
            num_match += 1

    pay = [0, 4, 7, 100, 50000, 1000000, 25000000]
    return pay[num_match]


def main():
    win = lot()
    income = 0
    losses = 0
    for i in range(1000000):
        tix = lot()
        losses += 2
        income += pay(tix, win)

    bal = income - losses
    over = income / losses
    print("Winnings: $" + str(income))
    print("Losses: $" + str(losses))
    print("Balance: $" + str(bal))
    print("Overall: $" + str(over))


main()
