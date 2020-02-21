"""
Lab 20: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean.
The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

1. 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
2. 4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
3. 5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
4. 10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
5. 1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
6. 85
7. 5
8. Valid!
"""
import string
card_in = input("Enter your card number: ")
if card_in.isdigit() == False:
    print("Must be a number.")
# elif len(card_in) <= 15 or len(card_in) >= 17:
#     print("Card length must be 16 digits")
else:
    card_in = list(map(int, card_in))

check_digit = card_in.pop(-1)


print(card_in)
card_in.reverse()
print(card_in)
double_even = [num * 2 if i%2==0 else num for i, num in enumerate(card_in)]
print(double_even)
sub_nine = [num - 9 if num > 9 else num for num in double_even]
print(sub_nine)
count = 0
for num in sub_nine:
    count += num
print(count)

count1 = [str(count)]
print(count1)
# str(count)
# count_split = list(map(int, count))
# print(count_split)
# card_check = count_split[-1]
# print(card_check)

if card_check == check_digit:
    print("Valid!")
else:
    print("Not Valid!")
