"""
Lab 17: Palindrome and Anagram
Let's write a palindrome and anagram checker.

Palindrome
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome

Anagram
Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
"""
# #Palindrome Lab
# def check_palindrome(x):
#     x = input("Type your word: ")
#     user_list = list(x.lower())
#     user_reverse = list(reversed(user_list))

#     if user_list == user_reverse:
#         return print(f"{x} is a palindrome")
#     return print(f"{x} is not a palindrome")

# check_palindrome("x")

# #End Palindrom Lab

# #Anagram Lab
# def check_anagram(x, y):
#     x = input("Enter your first word/phrase: ")
#     y = input("Enter your second word/phrase: ")
#     user_list = list(x.lower())
#     user_list2 = list(y.lower())

#     user_sorted = sorted(user_list)
#     user_sorted2 = sorted(user_list2)

#     if user_sorted == user_sorted2:
#         # print(f"{x} is an anagram of {y}")
#         return print(f"{x} is an anagram of {y}")
#     return print(f"{x} is not an anagram of {y}")

# check_anagram("x", "y")

# #End Palindrome Lab
