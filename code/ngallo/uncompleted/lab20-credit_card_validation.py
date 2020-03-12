import string
import math

test_card = []

def cc_checker(test_card):
## make test_card_list look like a list of ints
# test_card = [int(input("hello")) in a for loop]
    # test_card = int(input('enter your credit card number: '))
    # test_card = str(4012888888881881)
    test_card_list = [2,2,2,2,2]
    print(test_card)
    # if test_card.isdigit() == False:
    #     print("Must be a number!")
    #     cc_checker(test_card)
    print(test_card)
    # test_card_list = str(test_card)
    # test_card_list = list(test_card_list)
    print(f"test_card_list: {test_card_list}")

    pop_digit = test_card_list.pop()
    print(f"popped digit {pop_digit}")

    reversed_digits = test_card_list[::-1]
    print(f"reversed_digits: {reversed_digits}")

    for i in range(1, len(reversed_digits), 2):
        reversed_digits[i] *= 2
        if reversed_digits[i] >= 9:
            reversed_digits[i] - 9
    print(f"multiple_digits: {reversed_digits}")

    break
    return doubled_digit
cc_checker(test_card)

# visa test card number: 4012888888881881 

# Lab 20: Credit Card Validation
# Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

# 1234567890123456

# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is valid.
# For example, the worked out steps would be:

# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
# 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
# 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
# 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
# 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
# 85
# 5
# Valid!

'''
# 4012888888881881
def cc_check(cc_str):

    print('input: ', cc_str)

    cc_ints = [int(char) for char in cc_str]
    print(cc_ints)
    
    check_digit = cc_ints[-1]
    print('check digit: ', check_digit)

    cc_ints = cc_ints[:-1]
    print('all but last: ', cc_ints)

    reversed = cc_ints[::-1] 
    print('reversed', reversed)

    # this doubles every other starting with the first in the list
    reversed_doubled = [x*2 if idx % 2 == 0 else x for idx, x in enumerate(reversed)]
    print('reversed doubled', reversed_doubled)

    subtracted_list = [x-9 if x > 9 else x for x in reversed_doubled]
    print('subtracted', subtracted_list)

    summation = sum(subtracted_list)
    print('summation', summation)

    second_digit_str = [digit for digit in str(summation)][1]
    is_valid = check_digit == int(second_digit_str)S
    print(is_valid)

replaced = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'.replace(' ', '')
visa_test = '4012888888881881'
print(replaced)
cc_check(visa_test)
print('\n')
cc_check(replaced)
'''