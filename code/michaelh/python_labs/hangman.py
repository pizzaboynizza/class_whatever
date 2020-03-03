'''
# Group Exercise: Hangman

Let's write a program to play a game of hangman. In the data folder, you'll find `english.txt` which contains a list of several thousand english words. Write a function `load_words(path)` which reads the text from this file and return a list of strings which are greater than 5 letters. Randomly pick a word from that list and begin the game. Allow the user 10 tries to guess the letters of the word. Keep track of the letters the user has already guessed.

Show them a list of 'blanks' and ask them for a letter. If they guess a letter which is in the word, show the blanks with the letters filled in. If they guess a letter which is not in the word, tell them and subtract 1 from their remaining guesses. If they guess a letter they've guessed before, tell them and do **not** subtract 1 from their guesses.

Be kind, if the user can't guess the word in the number of allotted guesses, print the word and ask them if they'd like to play again.

Feel free to customize the user interface, but provide these minimum features. Below is an example run of the program.

```
_ _ _ _ _ _ _ _ _
# of guesses remaining: 10
already guessed: 

Guess a letter: a
_ a _ _ _ _ a _ _
# of guesses remaining: 10
already guessed: a

Guess a letter: a
You've already guessed that
_ a _ _ _ _ a _ _
# of guesses remaining: 10
already guessed: a

Guess a letter: k
_ a _ _ _ _ a _ _
# of guesses remaining: 9
already guessed: a, k
Guess a letter: 
```
'''
import random
def load_long_words():
    filename = 'dictionary.txt'
    with open('/home/michael/Desktop/pdxcode/class_whatever/code/michaelh/python_labs/'+filename, 'r') as f:
        contents = f.read()
    words = contents.split('\n')
    long_words = []
    for word in words:
        if len(word) > 5:
            long_words.append(word)
    return long_words

words = load_long_words()

rand_word = random.choice(words)
print(rand_word)
print('*'*len(rand_word))
guess_char = input('What is a letter in the word? ')
if guess_char in rand_word
    
# print(words[0])
# print(len(words))