## -- Group Lab - Hangman - 03/03/2020 - Joe Dean, Nick Gallo, Anthony Nwajei -- ##


import random
import string

## initial start up print:
print("**** Let\'s play Hangman ****")

## opens text file, gets words longer than 5 letters for play:
def import_function():
    with open('english.txt', 'r', encoding='utf-8') as file:
        contents_of_text = file.read().split('\n')
        words_greater_than_five = []
        for i in contents_of_text:
            if len(i) > 5:
                words_greater_than_five.append(i)
        return words_greater_than_five 

six_letter_words = import_function()

## prints out word for hangman game. Example _ _ a _ t _ _ _ :
def letter_check(word, guessed_letter):
    for letters in word:
        if letters in guessed_letter:
            print(letters, end=' ')
        else:
            print('_', end=' ')
    print('')

## checks if user has correctly guessed (or not) the random computer word:
def valid_letters(word, guessed_letters):
    for letters in word:
        if letters not in guessed_letters:
            return False
    return True

## print ascii 
def print_ascii(guesses):
    print(f"""
     ______
    |/    {'|'if guesses>=1 else' '}
    |    {'('if guesses>=2 else' '}{'_'if guesses>=3 else' '}{')'if guesses>=4 else' '}
    |    {'/'if guesses>=5 else' '}{'|'if guesses>=6 else' '}{chr(92)if guesses>=7 else' '}
    |     {'|'if guesses>=8 else' '}
    |    {'/'if guesses>=9 else' '} {chr(92)if guesses>=10 else ' '}
    |
    |
   _|__________ 
    """)

## hangman games bulk functionality:
def hangman(six_letter_words):
    number_of_guesses = 0
    guessed_list = []
    while number_of_guesses < 10:
        letter_check(six_letter_words, guessed_list)
        print("# of guesses remaining:", 10 - number_of_guesses)
        print(guessed_list)
        guessed_letter = input("Pick one of the 26 letters: ").lower()
        if guessed_letter not in guessed_list and guessed_letter in string.ascii_lowercase and len(guessed_letter) == 1:
            if guessed_letter not in six_letter_words:
                number_of_guesses += 1
            guessed_list.append(guessed_letter)
        elif guessed_letter not in string.ascii_lowercase or len(guessed_letter) > 1:
            print("Please pick a valid letter of the alphabet: ")
        else:
            print("You've already guessed this letter, please, pick another: ")
        if valid_letters(six_letter_words, guessed_list):
            print(f"You win! The word was {six_letter_words}.")
            return True
        print_ascii(number_of_guesses)
    print(f"Sorry, you lose! The word was {six_letter_words}.")
    return False




## this is the game's while loop, prompts the user to play again or ends game:
while True:
    hangman(random.choice(six_letter_words))
    user_yesno = input("Do you want to play again? ").lower()
    while user_yesno != "yes" and user_yesno != "no":
        user_yesno = input("Please enter yes or no:  ").lower()
    if user_yesno != "yes":
        break
## last thing to print when user is done playing:

print("Goodbye!")