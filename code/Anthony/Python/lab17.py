''' Palindrome
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome'''

word_input = input("Enter a word: ")
# word_input = input("Enter the word: ")

# def check_palindrome(word_input):
    
#     if word_input == word_input[::-1]:
#         return True
#     else:
#         return False
# print(check_palindrome(word_input))

#BETTER WAY BELOW
def check_palindrome(word_input):
    
    return word_input == word_input[::-1]
    print(f"{word_input} is a palindrome")
print(check_palindrome(word_input))


# version 2
user1 = input("Enter a word: ")
user2 = input("Enter another word: ")
user1 = user1.lower()
user2 = user2.lower()
user1 = user1.replace(' ', '')
user2 = user2.replace(' ', '')
user1 = sorted(user1)
user2 = sorted(user2)


def check_anagram(user1, user2):
    return user1 == user2
    
print(check_anagram(user1, user2))






