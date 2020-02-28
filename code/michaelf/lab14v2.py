import random

def pick6():
    x = [random.randint(1,99) for i in range(0,6)]
    return x

def num_matches(winner, pick):
    total = 0
    for i in range(0,6):
        if pick[i] == winner[i]:
            total += 1
        else:
            pass
    return total

def print_roi(earnings, expenses):
    print((earnings - expenses) /  expenses)

winner = pick6()
balance = 0
expenses = 0
earnings = 0
print(winner)

for i in range(0, 100000):
    pick = pick6()
    print(pick)
    balance -= 2
    expenses += 2


    total = num_matches(winner, pick)
    if total == 0:
        pass
    elif total == 1:
        balance += 4
        earnings += 4
    elif total == 2:
        balance += 7
        earnings += 7
    elif total == 3:
        balance += 100
        earnings += 100
    elif total == 4:
        balance += 50000
        earnings += 50000
    elif total == 5:
        balance += 1000000
        earnings += 1000000
    elif total == 6:
        balance += 25000000
        earnings += 25000000
    else:
        pass
    print(total)
    print(balance)

print(f"Your final balance is ${balance}")
print(f"Your expenses were ${expenses}, your earnings were ${earnings}, making your return on investment(ROI):")
print_roi(earnings, expenses)
    



