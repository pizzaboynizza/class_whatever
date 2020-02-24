# Lab 14
# Author : Joe
from random import randint

def pick6():
    ret = []
    for i in range(6):
        ret.append(randint(1, 99))
    return ret

def num_match(winner, ticket):
    matches = 0
    for i in range(6):
        if winner[i] == ticket[i]:
            matches += 1
    return matches


winner = pick6()
wins = [0, 0, 0, 0, 0, 0, 0]
games = 100000

for i in range(games):
    temp = pick6()
    wins[num_match(winner, pick6())] += 1

earnings = wins[1] * 4 + wins[2] * 7 + wins[3] * 100 + wins[4] * 50000 + wins[5] * 1000000 + wins[6] * 25000000
expenses = games * 2
balance = earnings - expenses
roi = (earnings - expenses) / expenses

for i in range(7):
    print(f"Games with {i} matches: {wins[i]}")

print(f"\nAfter {games} games:\n\tEarnings:\t {earnings}\n\tFinal Balance:\t{balance}\n\tROI:\t\t{roi}\n")