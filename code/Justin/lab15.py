#
# def convert_to_english(num):
#     if 0 <= num <= 99:
#         tens_digit = (num//10)
#         ones_digit = (num%10)
#
#     if ones_digit == 0 and tens_digit == 1:
#         print("ten")
#
#     elif ones_digit == 1 and tens_digit == 1:
#         print("eleven")
#
#     elif ones_digit == 2 and tens_digit == 1:
#         print("twelve")
#
#     elif ones_digit == 3 and tens_digit == 1:
#         print("thirteen")
#
#     elif ones_digit == 4 and tens_digit == 1:
#         print("fourteen")
#
#     elif ones_digit == 5 and tens_digit == 1:
#         print("fifteen")
#
#     elif ones_digit == 6 and tens_digit == 1:
#         print("sixteen")
#
#     elif ones_digit == 7 and tens_digit == 1:
#         print("seventeen")
#
#     elif ones_digit == 8 and tens_digit == 1:
#         print("eighteen")
#
#     elif ones_digit == 9 and tens_digit == 1:
#         print("nineteen")
#
#     a = ''
#     if ones_digit == 1:
#         a = "one"
#
#     elif ones_digit == 2:
#         a = "two"
#
#     elif ones_digit == 3:
#         a = "three"
#
#     elif ones_digit == 4:
#         a = "four"
#
#     elif ones_digit == 5:
#         a = "five"
#
#     elif ones_digit == 6:
#         a = "six"
#
#     elif ones_digit == 7:
#         a = "seven"
#
#     elif ones_digit == 8:
#         a = "eight"
#
#     elif ones_digit == 9:
#         a = "nine"
#
#     elif ones_digit == 0:
#         print(j)
#     b = ''
#     if tens_digit == 2:
#         print("twenty" + a)
#
#     elif tens_digit == 3:
#          print("thirty" + a)
#
#     elif tens_digit == 4:
#         print("forty" + a)
#
#     elif tens_digit == 5:
#         print("fifty" + a)
#
#     elif tens_digit == 6:
#         print("sixty" + a)
#
#     elif tens_digit == 7:
#         print("seventy" + a)
#
#     elif tens_digit == 8:
#         print("eighty" + a)
#
#     elif tens_digit == 9:
#         print("ninety" + a)
#
# convert_to_english(27)

def convert_to_english(num):
    if 100 <= num <= 999:
        hundreds_digit = (num//100)
        tens_digit = (num//10)
        ones_digit = (num%10)

    a = ''
    if ones_digit == 1:
        a = "one"

    elif ones_digit == 2:
        a = "two"

    elif ones_digit == 3:
        a = "three"

    elif ones_digit == 4:
        a = "four"

    elif ones_digit == 5:
        a = "five"

    elif ones_digit == 6:
        a = "six"

    elif ones_digit == 7:
        a = "seven"

    elif ones_digit == 8:
        a = "eight"

    elif ones_digit == 9:
        a = "nine"

    b = ''
    if tens_digit == 2:
        b = "twenty"

    elif tens_digit == 3:
         b = "thirty"

    elif tens_digit == 4:
        b = "forty"

    elif tens_digit == 5:
        b = "fifty"

    elif tens_digit == 6:
        b = "sixty"

    elif tens_digit == 7:
        b = "seventy"

    elif tens_digit == 8:
        b = "eighty"

    elif tens_digit == 9:
        b = "ninety"

    c = ''
    if hundreds_digit == 1:
        c = "one hundred"

    elif hundreds_digit == 2:
        c = "two hundred"

    elif hundreds_digit == 3:
        c = "three hundred"

    elif hundreds_digit == 4:
        c = "four hundred"

    elif hundreds_digit == 5:
        c = "five hundred"

    elif hundreds_digit == 6:
        c = "six hundred"

    elif hundreds_digit == 7:
        c = "seven hundred"

    elif hundreds_digit == 8:
        c = "eight hundred"

    elif hundreds_digit == 9:
        c = "nine hundred"


convert_to_english(999)









