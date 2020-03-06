'''
# Lab 17: Palindrome and Anagram

Let's write a palindrome and anagram checker.

## Palindrome

A palindrome is a word that's the same forwards or backwards, e.g. racecar. Another way to think of it is as a `word that's equal to its own reverse`.


Write a function `check_palindrome` which takes a string, and returns True if the string's a palindrome, or False if it's not.

```
>>> enter a word: racecar
>>> 'racecar' is a palindrome

>>> enter a word: palindrome
>>> 'palindrome' is not a palindrome
```

## Anagram

Two words are anagrams of eachother if the letters of one can be rearranged to fit the other. e.g. `anagram` and `nag a ram`.

Write another function `check_anagram` that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

1. Convert each word to lower case (`lower`)
2. Remove all the spaces from each word (`replace`)
3. Sort the letters of each word (`sorted`)
4. Check if the two are equal

```
>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams
```
'''
import string
def lower_rm_whitespace(org_str):
    new_str = ''
    new_str = org_str.lower()
    for char in string.whitespace:
        new_str = new_str.replace(char, '')
    return new_str

def mk_list(org_str):
    str_list = []
    for char in org_str:
        str_list.append(char)
    return str_list

def check_palindrome(org_str):
    lowered_str = lower_rm_whitespace(org_str)
    lowered_str_list = mk_list(lowered_str)
    rev_str_list = lowered_str_list.copy()
    rev_str_list.reverse()
    # print(lowered_str_list)
    # print(rev_str_list)    

    for i in range(len(lowered_str_list)):
        if rev_str_list[i] != lowered_str_list[i]:
            return False
    return True

def check_anagram(org_str1, org_str2):
    lowered_str1 = lower_rm_whitespace(org_str1)
    lowered_str1_list = mk_list(lowered_str1)

    lowered_str2 = lower_rm_whitespace(org_str2)
    lowered_str2_list = mk_list(lowered_str2)    

    lowered_str1_list.sort()
    lowered_str2_list.sort()
    for i in range(len(lowered_str1_list)):
        if lowered_str1_list != lowered_str2_list:
            return False
    return True            

# while True:
#     palindrome = input('Enter a word: ')
#     if palindrome == 'done':
#         break

#     # print(bool(check_palindrome(palindrome)))
#     if check_palindrome(palindrome):
#         print(f'\'{palindrome}\' is a palindrome.')
#     else:
#         print(f'\'{palindrome}\' is not an pralindrome.')

while True:
    anagram1 = input('Enter a word: ')
    anagram2 = input('Enter another word: ')

    if anagram1 == 'done' or anagram2 == 'done':
        break

    if check_anagram(anagram1, anagram2):
        print(f'\'{anagram1}\' is an anagram of \'{anagram2}\'.')
    else:
        print(f'\'{anagram1}\' is not an anagram of \'{anagram2}\'.')
