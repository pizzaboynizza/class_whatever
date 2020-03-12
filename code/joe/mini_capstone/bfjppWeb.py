import requests
import re
import random
from draw import showMessage


width, height = 1200, 600 # ensure same as in bfjpp


def getPrograms(): # load all programs from EgoJSout
    page = requests.get("http://codu.org/eso/bfjoust/in_egobot/").text

    programs = ["[RANDOM]", "[FILE]"] # include these for a random selection and a file selection

    i = 0
    while i < len(page):
        temp = re.search(r'"\w+\.bfjoust"', page[i:]) # find the name of the program
        if temp != None:
            programs.append(temp.group()[1:-9])
            i += temp.end()
        else:
            i += 1

    return programs

# get the name of the program chosen; choose randomly if random, get a filename if file, do nothing special otherwise
def programName(name, screen, font):
    if name == "[RANDOM]":
        return random.choice(getPrograms()[2:])
    if name == "[FILE]":
        while True: # must enter an actual file
            try:
                showMessage("Enter filename in terminal", screen, font, (0x0, 0xFF, 0x0), width, height)
                filename = input("Enter filename: ")
                with open(filename) as file:
                    pass
                return "/" + filename
            except:
                print("That file does not exist!")
    return name

# get the actual program
def loadProgram(name):
    if name[0] == "/": # if a file, load as a file
        with open(name[1:]) as file:
            return file.read()
    else: # otherwise, it's on EgoJSout; it should all be plaintext
        return requests.get(f"http://codu.org/eso/bfjoust/in_egobot/{name}.bfjoust").text