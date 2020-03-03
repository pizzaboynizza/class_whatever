'''Write a program that prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Index	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24	25
English	a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z
ROT+13	n	o	p	q	r	s	t	u	v	w	x	y	z	a	b	c	d	e	f	g	h	i	j	k	l	m '''
english_alphabets = 'abcdefghijklmnopqrstuvwxyz'  #list of alphabets
input_string = input(" Enter a string: ")
key = int(input("Enter a key: "))
output_string = ' '
n = len(input_string) #length of the input string

for i in range(n):
    # print (i)
    character = input_string[i]
    # print(character)
    char_location = english_alphabets.find(character)
    # print(character, char_location)
    new_location = (char_location + key) %26
    print(character, char_location, new_location)


    # VERSION 2
    # USE COUNTER?????????