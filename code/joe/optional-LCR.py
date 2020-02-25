# Lab : LCR Simulator
# Author : Joe

from random import choice

# player list:
#   {playername : [chips, playername_right, playername_left]}

start_chips = 3

def rollDice():
    return choice([".", ".", ".", "l", "r", "c"])

def passLeft(playerlist, player):
    playerlist[player][0] -= 1
    playerlist[playerlist[player][2]][0] += 1

def passRight(playerlist, player):
    playerlist[player][0] -= 1
    playerlist[playerlist[player][1]][0] += 1

def takeTurn(playerlist, player):
    dice = [rollDice() for i in range(3 if playerlist[player][0] > 2 else playerlist[player][0])]
    center = 0
    for check in dice:
        if check == "l":
            passLeft(playerlist, player)
        elif check == "r":
            passRight(playerlist, player)
        elif check == "c":
            playerlist[player][0] -= 1
            center += 1
    return center

def makePlayList(proto):
    ret = {}
    ret[proto[0]] = [start_chips, "", ""]
    prev = proto[0]
    for i in range(1, len(proto)):
        ret[proto[i]] = [start_chips, "", prev]
        ret[prev][1] = proto[i]
        prev = proto[i]
    ret[proto[-1]][1] = proto[0]
    ret[proto[0]][2] = proto[-1]
    return ret

def checkEnd(playerlist):
    still_in = 0
    for n in playerlist.values():
        if n[0] != 0:
            still_in += 1
    if still_in > 1:
        return False
    else:
        return True

players = []
temp = "."
while temp != "" or len(players) < 2:
    temp = input("Enter player name (or nothing to finish): ")
    if temp != "":
        players.append(temp)

players = makePlayList(players)

while True:
    for p in players.keys():
        players[p][0] = start_chips

    center = 0
    turns = 0

    while not checkEnd(players):
        for p in players.keys():
            center += takeTurn(players, p)
            turns += 1
            if checkEnd(players):
                break

    winner = ""
    for p in players.keys():
        if players[p][0] != 0:
            winner = p
            break

    print(f"After {turns} turns, {winner} won with {players[winner][0]} chips and {center} chips in the center.\n")

    temp = input("Play again?(y/n) ")
    if not(len(temp) > 0 and temp[0].lower() == "y"):
        break

print("Goodbye!")