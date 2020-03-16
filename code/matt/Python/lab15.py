"""
Lab 15: Number to Phrase
Convert a given number into its english representation. For example: 67 becomes 'sixty-seven'. 
Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.

x = 67
tens_digit = x//10
ones_digit = x%10
Hint 2: use the digit as an index for a list of strings OR as a key for a dict of digit:phrase pairs.

Version 2
Handle numbers from 100-999.

Version 3 (optional)
Convert a number to roman numerals.

Version 4 (optional)
Convert a time given in hours and minutes to a phrase.
"""
translation_teens = {
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

translation_tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

translation_ones = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero"
}
# convert number to text
while True:
    user_num = int(input("What's your number? "))
    if user_num in [20, 30, 40, 50, 60, 70, 80, 90]:
        fdigit = user_num//10
        print(f"{translation_tens[fdigit]}")
        continue
    elif 0 <= user_num < 10:
        print(f"{translation_ones[user_num]}")
        continue
    elif 10 <= user_num <= 19:
        print(f"{translation_teens[user_num]}")
        continue
    elif 21 <= user_num < 100:
        fdigit = user_num//10
        sdigit = user_num%10    
        print(f"{translation_tens[fdigit]}-{translation_ones[sdigit]}")
        continue
    elif user_num == 100:
        print("one hundred")
    elif user_num in [110, 120, 130, 140, 150, 160, 170, 180, 190]:
        sub_100 = user_num - 100
        fdigit = sub_100//10
        print(f"one hundred {translation_tens[fdigit]}")
    elif 100 < user_num < 110:
        sub_100 = user_num - 100
        print(f"one hundred {translation_ones[sub_100]}")
    elif 110 <= user_num <= 119:
        sub_100 = user_num - 100
        print(f"one hundred {translation_teens[sub_100]}")
    elif 120 <= user_num < 200:
        sub_100 = user_num - 100
        fdigit = sub_100//10
        sdigit = sub_100%10
        print(f"one hundred {translation_tens[fdigit]}-{translation_ones[sdigit]}")
        continue
    else:
        print("Must be a number between 0 - 199.")
        break

