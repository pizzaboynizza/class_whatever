def anagram_checker():
    string_one = input("enter a word ")

    string_one_lower = string_one.lower()

    removed_one = string_one_lower.replace(' ', '')

    reversed_one = removed_one[::-1]

    if string_one == reversed_one:
        print("Anagram!")
    else:
        print("Negative")
    
    user_input = input("Do you want to play again? ")
    if user_input == "yes":
        anagram_checker()
    else:
        print("Have a good one! ")

anagram_checker()

# Lab 17: Palindrome and Anagram
# Let's write a palindrome and anagram checker.

# Palindrome
# A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

# Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.

# >>> enter a word: racecar
# >>> 'racecar' is a palindrome

# >>> enter a word: palindrome
# >>> 'palindrome' is not a palindrome

'''

def anagram_checker():
    string_one = input("enter a word ")
    string_two = input("enter another word ")

    string_one_lower = string_one.lower()
    string_two_lower = string_two.lower()


    removed_one = string_one_lower.replace(' ', '')
    removed_two = string_two_lower.replace(' ', '')

    sorted_one = sorted(removed_one)
    sorted_two = sorted(removed_two)

    if sorted_one == sorted_two:
        print("Anagram!")
    else:
        print("Negative")
    
    user_input = input("Do you want to play again? ")
    if user_input == "yes":
        anagram_checker()
    else:
        print("Have a good one! ")

anagram_checker()

'''

# Anagram
# Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. anagram and nag a ram.

# Write another function check_anagram that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

# Convert each word to lower case (lower)
# Remove all the spaces from each word (replace)
# Sort the letters of each word (sorted)
# Check if the two are equal
# >>> enter the first word: anagram
# >>> enter the second word: nag a ram
# >>> 'anagram' and 'nag a ram' are anagrams