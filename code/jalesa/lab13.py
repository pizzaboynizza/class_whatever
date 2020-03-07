'''Lab 13: ROT Cipher
Write a program that prompts the user for a string,
 and encodes it with ROT13. For each character, 
 find the corresponding character, add it to an
  output string. Notice that there are 26 letters 
  in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
Version 2 (optional)
Allow the user to input the amount of rotation used in the encryption / decryption.'''

# import string module and ascii_lowercase so that i wont have to 
# make a list of alphabets
# save lowercase letters into a variable so that i can make it into a list.
import string
from string import ascii_lowercase
letters = string.ascii_lowercase
# print(ascii_lowercase)

# make empty list outside of for loop because it has to be 
# defined before you use it in a for loop otherwise for loop does not recognize it.
# for i in user_input: means -- everytime you go throuh a letter in user_input
# new.append(ascii_lowercase.index(i))  
# means --- add the index of the lower_case letters to my empty list named new.
user_input = input("Enter a word: ") 
new = []
for i in user_input:
  new.append(ascii_lowercase.index(i))
print(new)


    #  modules 26 is used to go from z back to a. 
    # It takes the remainder which will put you back at the beginning
    # of the alphabet after z.
    # if the number is 26 and below % 26 will not effect the summation 
    # of (g + 13)
    # append the summation of (g + 13)%26 to my empty list.
    
rot13_index = []
for g in new:
    new1 = (g + 13)%26
    rot13_index.append(new1)
print(rot13_index)



# x can be anything it will go through each item in rot13_index
# every time we iterate to a new item in rot_13 append itll add to a.
# print a 
a = []
for x in rot13_index:
  a.append(letters[x])
print(a)






