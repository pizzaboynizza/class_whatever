# Lab 15 (verions 1-3)
# Author : Joe

num = input("Enter number from 0-999: ")
while not num.isdigit() or len(num) > 3:
    num = input("Must enter a number from 0-999: ")
num = int(num)

single_digit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
double_digit = ["", "UNUSED", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens_case = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

ones_place = num % 10
tens_place = (num // 10) % 10
hundreds_place = num // 100

full_num = ""

if hundreds_place != 0:
    full_num = single_digit[hundreds_place] + " hundred "

if tens_place == 1:
    full_num += teens_case[ones_place]
elif num == 0:
    full_num = "zero"
else:
    full_num += double_digit[tens_place] + (" " if tens_place != 0 and ones_place != 0 else "") + single_digit[ones_place]

# Roman Numerals (version 3)
rome_single = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
rome_double = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
rome_triple = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]

if num == 0:
    rome_num = "nulla"
else:
    rome_num = rome_triple[hundreds_place] + rome_double[tens_place] + rome_single[ones_place]

#Result
print(f"{num} is:\n\t{full_num}\n\t{rome_num}")