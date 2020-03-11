'''
Nick Barker
Lab 17
Palindrome/Anagram Checker

Palindrome
and
Anagram
'''
import time

#variable, this will be a string!
posspal = input("Please enter your possible palidrome: ")

#for fun
print("Great work!")
print("computing..")
time.sleep(2)
print("computing..")
time.sleep(2)

#remind user of the variable
print(posspal)
#show inverse
foo = (posspal[::-1])
print(foo)

#function time!
def check_palindrome(posspal, foo):
    if posspal == foo:
        print("We have a match!")
        return("True!")
    elif posspal != foo:
        print("Not a match! Launching Missles!")
        return("False!")

#call that puppy!
check_palindrome(posspal, foo)
