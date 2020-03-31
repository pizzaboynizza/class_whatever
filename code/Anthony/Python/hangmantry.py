#open and read english.txt file
import string 
import random
with open('english.txt', 'r') as f:
    text= f.read()

path = []
guess =
def valid_words(words):
    word = random.choice(words) #randomly choses words from list of 'path'
    while '-'in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = valid_words(words)
    word_letters = set(words) #SAVES ALL GUESSED LETTERS IN HERE
    alphabets = set(string.ascii_upper)
    guessed_letters = set() #THIS IS USED TO SAVE ALL LETTERS USER ALREADY GUESSED
    
while len(word_letters) == 0
user_input = input("Guess the letters: ")
if user_input in alphabets-guessed_letters:
    guessed_letters.add(user_input)
    if user_input in word_letters:
        word_letters.remove(user_input) #REMOVES THE CORRECT GUESSED LETTER FROM THE LIST CORRECT LETTERS IN THE WORD
elif user_input in guessed_letters:
    print("You alreadt guessed that letter{guessed[user_input]}")
else:
    print("Entered letter invalid")


