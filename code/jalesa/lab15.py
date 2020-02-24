# Lab 15: Number to Phrase
# Convert a given number into its english representation.
# For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
# Hint: you can use modulus to extract the ones and tens digit.

user_input = int(input("Enter a number 0-99: "))
tens_digit = user_input//10
ones_digit = user_input%10


collection = {1:"one", 2:"two", 3:'three', 4:"four", 5:"five",
6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven",
12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
16:"sixteen", 17:"seventeen", 18:"eighteen",  19:"nineteen", 
20:"twenty", 30:"thirty", 40:"fourty",  50:"fifty", 60:"sixty",
70:"seventy", 80:"eighty", 90:"ninety", 100:"onehundred",
}

collection_2 = {1:"one", 2:"two", 3:'three', 4:"four", 5:"five",
6:"six", 7:"seven", 8:"eight", 9:"nine"}

val1 = user_input/tens_digit 
val2 = user_input/ones_digit 

if user_input > 20:
    print(f"{collection[user_input] / tens_digit} + {collection_2[user_input] / ones_digit}")



# collection[val1] = collection[4] = 'four'
# collection[val2] = collection[5] = 'five'

# concat = val + val2
 

# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings 
# OR as a key for a dict of digit:phrase pairs.



# Version 2
# Handle numbers from 100-999.

# Version 3 (optional)
# Convert a number to roman numerals.

# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase.