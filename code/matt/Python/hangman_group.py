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
winning_word = random.choice(words)
winning = list(winning_word)

for letter in winning:
    blanks.append("_ ")

while blanks != winning:
    print(blanks)
    print(f"Guessed: {guesses}")
    user_in = input("What letter do you guess?: ")
    if user_in in guesses:
        print("You've already guessed this letter!")
        print(f"You have {counter} guesses remaining.")
    elif user_in in winning:
        for i, char in enumerate(winning):
            if user_in == char:
                blanks[i] = char
        guesses.append(user_in)
        print("That's in the word!")
        print(f"You have {counter} guesses remaining.")
    elif user_in not in winning:
        counter -= 1
        guesses.append(user_in)
        print(f"{user_in} not in the word!")
        print(f"You have {counter} guesses remaining.")
    elif counter == 0:
        print("You ran out of tries!")
        print(f"The winning word was {winning_word}")
    else:
        print("something went wrong")
else:
    print(f"You win! The word was {winning_word} and you had {counter} guesses remaining!")

