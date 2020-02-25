#Palindrome
'''
A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a word that's equal to its own reverse.

Write a function check_palindrome which takes a string, and returns True if the string's a palindrome, or False if it's not.
'''







#ANNAGRAM
word_one = input("Enter a word (in lowercase): ")
word_two = input("Enter another word (in lowercase): ")
def check_annagram(word_one, word_two):
  print(sorted(word_one), sorted(word_two))
if sorted(word_one) == sorted(word_two):
  print("True")
else:
  print("False")


'''
def anagram(word):
    word = word.lower().replace(" ", "")
    return word

def sort_word(word):
    word = list(word)
    word.sort()
    word = str(list_word)
    return word
one = input("Please enter a word: ")
two = input("Please enter another word: ")
anna1 = annagram(one)
anna2 = annagram(two)

sorted_anna1 = sort_word(anna1)
sorted_anna2 = sort_word(anna2)
print(one, two)
print(anna1, anna2)

if sorted_anna1 == sorted_anna2:
    print(f"{one} and {two} are anagrams")
else:
    print(f"{one} and {two} are not anagrams")
'''