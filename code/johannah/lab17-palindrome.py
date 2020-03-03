'''
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.
'''


word_one = input("Enter a word or phrase: ")
word_two = input("Enter another word or phrase: ")
first = word_one.replace(" ", "")
second = word_two.replace(" ", "")
lower_one = first.lower()
lower_two = second.lower()
# print(lower_one)
# print(lower_two)
one_reverse = lower_one[::-1]
two_reverse = lower_two[::-1]
# print(one_reverse)
# print(two_reverse)

# def check_palindrome(word_one, word_two):

if one_reverse == two_reverse:
  print("True")
else:
  print("False")