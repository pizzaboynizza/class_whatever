import random

with open('english.txt', 'r') as file:
    lines = file.read().split("\n")

words = []
guesses = []
blanks = []
counter = 10

for word in lines:
    if len(word) > 5:
        words.append(word)

winning = list(random.choice(words))

for letter in winning:
    blanks.append("_ ")

while blanks != winning:
    print(blanks)
    print(winning)
    user_in = input("What letter do you guess?: ")
    print(f"Guessed: {guesses}")
    print(f"You have {counter} guesses remaining.")
    if user_in in guesses:
        print("You've already guessed this letter!")
    elif user_in in winning:
        for i, char in enumerate(winning):
            if user_in == char:
                blanks[i] = char
        print("That's in the word!")
        print(f"You have {counter} guesses remaining.")
    elif user_in not in winning:
        counter -= 1
        guesses.append(user_in)
        print(f"{user_in} not in the word!")
    else:
        print("something went wrong")

