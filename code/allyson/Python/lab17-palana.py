# Quick Anagrams ##
'''
Let's try here
'''

print('Anagram Checker')

import string
def clear(x,y):
	x.clear()
	y.clear()
def check(x,y):
	if x == y:
		print("Match!")
	elif x != y:
		print("Mis-Match!")	

x=input("Word one: ").lower()
x=str(x)
y=input("Word two: ").lower()
y=str(y)

##List##
x=list(x)

y=list(y)

##Sort##
x=sorted(x)
y=sorted(y)

#Join#
x="".join(x)
y="".join(y)

##Run##
check(x,y)

print('Palindrome Checker')
import random

s=input('-->   ').lower()

def luna(s): 
    return s[::-1] 
  
def sol(s): 
    l = luna(s) 
    if (s == l): 
        return True
    return False
  

ans = sol(s) 
  
if ans == 1: 
    print(f'{s} is an anagram.') 
else: 
    print(f'{s} is not an anagram.') 

