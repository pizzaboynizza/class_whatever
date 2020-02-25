''' Palindrome
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome'''

# word_input = input("Enter a word: ")
# word_input = input("Enter the word: ")

# def check_palindrome(word_input):
    
#     if word_input == word_input[::-1]:
#         return True
#     else:
#         return False
# print(check_palindrome(word_input))


'''Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

Convert each word to lower case (lower)
Remove all the spaces from each word (replace)
Sort the letters of each word (sorted)
Check if the two are equal
>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams'''

list1 = 'anagram'
list2 ='nagaram'
sort_list1 = sorted(list1)
sort_list2 = sorted(list2)

# print(sort_list1)
# print(sort_list2)


def check_anagram():
    if sort_list1== sort_list2:
        return True
    else:
        return False
print(check_anagram())



