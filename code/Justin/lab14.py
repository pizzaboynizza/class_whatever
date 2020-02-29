

def lottery_numbers():

    list = [45, 7, 23, 76, 22, 1]

    import random

    list.sort()

    list2 = []

    for i in range(0, 6):
        number = random.randint(1, 99)
        list2.append(number)
        while number in list2:
            number = random.randint(1, 99)


    list2.sort()

    def common(list, list2):
        c = [value for value in list if value in list2]
        return c

    d = common(list, list2)

    num = 0

    while num <= 100000:

        profit = 0

        if len(d) == 1:
            profit += 4

        elif len(d) == 2:
            profit += 7

        elif len(d) == 3:
            profit += 100

        elif len(d) == 4:
            profit += 50000

        elif len(d) == 5:
            profit += 1000000

        elif len(d) == 6:
            profit += 25000000

        else:
            profit += -2
        num += 1

        profit_string = str(profit)

        print("Your profit in dollars is " + profit_string)
        break

lottery_numbers()
