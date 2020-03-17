import random

bigWords = []
guessletter = []
def goalWord():
    with open("english.txt","r") as allWords:
        wordList = allWords.read()
        wordList = wordList.split()
        for word in wordList:
            if len(word) > 5:
                bigWords.append(word)      

goalWord()

answer = random.choice(bigWords)
print(answer)

word = answer

def game():
    guessed = []
    wrong = []
    tries = 10
    while tries > 0:
        out = ''
        for letter in word:
            if letter in guessed:
                out = out + letter
            else:
                out = out + "_"

        if out == word:
            break

        print("guess the word:", out)
        # print(tries,"left")

        guess = input("Pick a letter: ")

        if guess in guessed or guess in wrong:
            print(f"You already guessed these letter {wrong}")
        elif guess in word:
            print("yay")
            guessed.append(guess)
        else: 
            print("nope")
            tries = tries - 1
            wrong.append(guess)
            print(tries)
        
        print()

    if tries:
        print("you guessed", word)
    else:
        print(f"you guessed wrong, this was the {word}")
    

   
while True:
    answer = input("do you want to play? ")
    if answer == 'yes':
        game()
    elif answer == 'no':
        break


    







