import requests
import re
import random



def getPrograms():
    page = requests.get("http://codu.org/eso/bfjoust/in_egobot/").text

    programs = ["[RANDOM]", "[FILE]"]

    i = 0
    while i < len(page):
        temp = re.search(r'"\w+\.bfjoust"', page[i:])
        if temp != None:
            programs.append(temp.group()[1:-9])
            i += temp.end()
        else:
            i += 1

    return programs


def programName(name):
    if name == "[RANDOM]":
        return random.choice(getPrograms()[2:])
    if name == "[FILE]":
        while True:
            try:
                filename = input("Enter filename: ")
                with open(filename) as file:
                    pass
                return "/" + filename
            except:
                print("That file does not exist!")
    return name


def loadProgram(name):
    if name[0] == "/":
        with open(name[1:]) as file:
            return file.read()
    else:
        return requests.get(f"http://codu.org/eso/bfjoust/in_egobot/{name}.bfjoust").text


# print(getPrograms())
# name = random.choice(getPrograms())
# print(name)
# print(loadProgram(name))

