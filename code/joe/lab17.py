# Lab 17
# Author : Joe

import string

# format string
def frmt(str):
    str = str.lower()
    if not str.isalpha():
        for c in (string.punctuation + string.whitespace):
            str = str.replace(c, "")
    return str

def anagram(str1, str2):
    str1 = list(frmt(str1)).sort()
    str2 = list(frmt(str2)).sort()
    return str1 == str2

def palindrome(istr):
    istr = list(frmt(istr))
    temp = istr.copy()
    temp.reverse()
    return temp == istr

words = []

while True:
    temp = input("Enter word or phrase (enter nothing to stop): ")
    if temp == "":
        if len(words) < 1:
            print("You must enter at least one word!")
        else:
            break
    else:
        words.append(temp)

print("\nChecking for palindromes...\n")

for word in words:
    if palindrome(word):
        print(f"\"{word}\" is a palindrome")

print("\nChecking for anagrams...\n")

if len(words) > 1:
    for i in range(len(words) - 1):
        for x in range(i+1, len(words)):
            if anagram(words[i], words[x]):
                print(f"\"{words[i]}\" is an anagram of \"{words[x]}\"")
else:
    print("\nOnly one word entered, cannot check for anagrams.\n")