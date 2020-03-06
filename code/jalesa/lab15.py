# Lab 15: Number to Phrase and Version 2
# Convert a given number into its english representation.
# For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.
# Hint: you can use modulus to extract the ones and tens digit.
# x = 67
# tens_digit = x//10
# ones_digit = x%10
# Hint 2: use the digit as an index for a list of strings 
# OR as a key for a dict of digit:phrase pairs.

# Handle numbers from 100-999.


collection = {1:"one", 2:"two", 3:'three', 4:"four", 5:"five",
6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten", 11:"eleven",
12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen",
16:"sixteen", 17:"seventeen", 18:"eighteen",  19:"nineteen", 
20:"twenty", 30:"thirty", 40:"fourty",  50:"fifty", 60:"sixty",
70:"seventy", 80:"eighty", 90:"ninety", 100:"onehundred", 
200:"two-hundred", 300: "three-hundred", 400:"four-hundred", 
500:"five-hundred", 600:"six-hundred", 700:"seven-hundred",
800:"eight-hundred", 900:"nine-hundred"
}

user_input = int(input("Enter a number 0-99: "))
if user_input == 1000:
   user_input = int(input("Enter a number 0-99: ")) 
elif user_input < 20:
    print(collection[user_input])
elif user_input > 100:
    ones_digit = user_input % 10
    print(ones_digit)
    tens_digit = user_input % 100
    print(tens_digit)
    hundred_digit = user_input // 100
    print(hundred_digit)
    tens_digit = tens_digit // 10
    print(tens_digit)
    a = tens_digit * 10
    print(a)
    b = hundred_digit * 100
    print(b)
    print(collection[b],"and", collection[a], collection[ones_digit])
else:
    print("Have a good day.")


 



# Version 3 (optional)
# Convert a number to roman numerals.

# Version 4 (optional)
# Convert a time given in hours and minutes to a phrase.