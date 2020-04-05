from pprint import pprint

with open("contactinfo.csv", "r") as file:
    lines = file.read().split("\n")

players = []
header = lines.pop(0).split(",")


def contacts(x):
    for each in range(len(lines) - 1):
        player = lines.pop(0)
        player = player.split(",")
        players.append(dict(zip(header, player)))
    return players


players = contacts(players)


def add(players):
    service = input("Chat Service?--->")
    sn = input("Screen Name?--->")
    tz = input("Time Zone?--->")
    game = input("Current Game?--->")
    server = input("Current Server?--->")
    new = []
    new.append(service)
    new.append(sn)
    new.append(tz)
    new.append(game)
    new.append(server)
    new = dict(zip(header, new))
    players.append(new)
    return players


def find(players):
    sn = input("Who are you looking for?--->")
    for i in range(len(players)):
        if players[i]["sn"] == sn:
            return players[i]


def change(players):
    sn = input("Who are you changing?--->")
    changes = input("What field do you need to change?--->")
    update = input(f"What are we changing {changes} to?--->")
    for i in range(len(players)):
        if players[i]["sn"] == sn:
            up_changes = players[i]
            up_changes[changes] = update
    return players


def delete(x):
    sn = input("Remove who?--->")
    for i in range(len(players)):
        if players[i]["sn"] == sn:
            players.pop(i)
    return players


def main(players):
    while True:
        print(
            "****<(^w^)>*******+*+*+*+*+(>^-^)> GAMING CONTACTS <(^-^<)*+*+*+*+*+********<(^w^)>****"
        )
        print(
            "[1] VIEW ALL    [2] SEARCH    [3] ADD    [3]UPDATE    [4]DELETE    [0] FINISH AND CLOSE"
        )
        call = input(">>>>>>")
        if call == "0":
            print("Thank You!  Goodbye!")
            with open('contactinfo.csv,"w",newline="\n') as file:
                file.write(",".join(players[0].keys()))
                file.write("\n")
                for each in players:
                    file.write(",".join(each.values()))
                    file.write("\n")
            break
        elif call == "1":
            for i, player in enumerate(players, 1):
                print(i, player)
        elif call == "2":
            print("Search Engine.")
            find(players)
        elif call == "3":
            add(players)
        elif call == "4":
            delete(players)
