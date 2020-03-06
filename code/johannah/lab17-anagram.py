'''
Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

1. Convert each word to lower case (lower)
2. Remove all the spaces from each word (replace)
3. Sort the letters of each word (sorted)
4. Check if the two are equal
'''


word_one = input("Enter a word or phrase: ")
word_two = input("Enter another word or phrase: ")
first = word_one.replace(" ", "")
second = word_two.replace(" ", "")
sorted_one = sorted(first.lower())
sorted_two = sorted(second.lower())

# def check_annagram(word_one, word_two):

if sorted_one == sorted_two:
  print("True")
else:
  print("False")