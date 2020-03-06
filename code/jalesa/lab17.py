'''
Let's write a palindrome and anagram checker.

Palindrome
A palindrome is a word that's the same forwards or 
backwards, e.g. racecar. Another way to think of it 
is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string,
 and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome'''

'''
user_input is to to be passed inside the function for the 
function to work
if user_input is not passed into the function
this ---> user_input = input("enter a mutha-fucking word: ")
must be under the function.
user_input = input("enter a mutha-fucking word: ")
'''

# ANSWER
def check_palindrome(user_input):
    if user_input == user_input[::-1]:
        return True
    else:
        return False

print(check_palindrome(user_input))

    




# Anagram
# Two words are anagrams of eachother if the letters
#  of one can be rearranged to fit the other. e.g. anagram and nag a ram.

# Write another function check_anagram that takes 
# two strings as parameters and returns True if they're
#  anagrams of eachother, False if they're not. 
# The procedure for comparing the two strings is as follow:

# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal
# >>> enter the first word: anagram
# >>> enter the second word: nag a ram
# >>> 'anagram' and 'nag a ram' are anagrams


def getInput():
    user_input = input("enter a mutha-fucking word: ")
    user_input.lower()
    user_input.replace(" ", "")
    sorted_input = sorted(user_input)
    print(sorted_input)
    return sorted_input

input1 = getInput()
input2 = getInput()


if input1 == input2:
    print(True)


# user_input2 = input("enter a mutha-fucking word: ")
# user_input2.lower()
# user_input.relace(" ", "")

# def check_palindrome(user_input, user_input2):
#     if user_input == user_input2:
#         return True
