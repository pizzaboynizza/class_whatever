from string import ascii_lowercase

user_input = str(input("Input a single word for encryption key: "))
user_value = int(input("How many rotations would you like to encrypt by? "))

user_append_input = []

## this for loop takes each letter/string in user_input, finds the ascii index and then appends it to user_append_input which is a global empty list.
for letter in user_input:
    user_append_input.append(ascii_lowercase.index(letter))
print(user_append_input)

## taking the index of each letter/number in user_append_input, adding 13 to that index.
new_index = [i + user_value for i in user_append_input]


## this variable is taking each letter's index and finding out if it is over 26. If the number is over 26 then it is using modulus to find the remainder. 
rotated_index = [i%26 for i in new_index]

final_list = []

for i in rotated_index:
    final_list.append(ascii_lowercase[i])

printed_value = "".join(final_list)

print(new_index)
print(rotated_index)
print(final_list)
print(printed_value)


# Lab 13: ROT Cipher

# Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

# Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
# English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
# ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m
# Version 2 (optional)
# Allow the user to input the amount of rotation used in the encryption / decryption.