"""
Lab 13: ROT Cipher
Write a program that prompts the user for a string, and encodes it with ROT13.
For each character, find the corresponding character, add it to an output string.
Notice that there are 26 letters in the English language, so encryption is the same as decryption.
Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
"""
import string
# eng = {0: "a",	1: "b",	2: "c",	3: "d",	4: "e",	5: "f", 6: "g", 7: "h",	8: "i",	9: "j", "10": "k", 11:"l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r", 18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z"}
alphabet_lower = list(string.ascii_lowercase)

user_in = input("Type your phrase: ")
user_out1 = []
user_word = list(user_in)

for letter in user_word:
    letter_test = alphabet_lower.index(letter)
    rot13 = letter_test + 13
    user_num = rot13 % 26 if rot13 > 26 else rot13
    user_out = alphabet_lower[user_num]
    user_out1.append(user_out)
    str(user_out1)
print("".join(user_out1))

# Still have to write allowing user to set rotation number instead of 13.