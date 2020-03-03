import random

with open("english.txt", 'r') as file:
    lines = file.read().split('\n')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

bigWords = []
word = []
def goalWord():
    with open("english.txt","r") as allWords:
        wordList = allWords.read()
        wordList = wordList.split()
        for word in wordList:
            if len(word) > 5:
                bigWords.append(word)      

goalWord()

bird = random.choice(bigWords)
print(bird)


def hangMan():					
  word = bird				
  blanks = "_"*len(word)	
  blanks_list = list(blanks) 
  new_blanks_list = list(blanks)
  guess_list = []


guess = input("Letter: ")





