'''
prompts the user for a string, and encodes it with ROT13. For each character, find the corresponding character, add it to an output string
'''

user_input = input("Enter something (letters only) to find out each character's ROT13 correspondence: ")
#add 13 to index except when more than 25 loop to 0 (0 = 26)
#modulus 26????
for i in range(26):
  print((i + 13) % 26)

'''
dictionary
chars = "abcdefghijklmnopqrstuvwxyz"
for char in chars:
  i + 13 < i=26
  if i > 25:
    26 = i 0
    27 = 1
    28 = 2
    29 = 3
    30 = 4
    31 = 5
    32 = 6
    33 = 7
    34 = 8
    35 = 9
    36 = 10
    37 = 11
    25 = 12
'''