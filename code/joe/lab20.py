#Lab 20
#Author : Joe

user_in = input("Enter credit card number: ")
while not user_in.isdigit() or len(user_in) < 13 or len(user_in) > 19:
    if not user_in.isdigit():
        user_in = input("Invalid number. Please try again: ")
    else:
        user_in = input("Credit card numbers must be between 13 and 19 digits: ")

#Step 1 : Convert the input string into a list of ints
ccn = [int(n) for n in user_in]

#Step 2 : Slice off the last digit. That is the check digit.
check_digit = ccn[-1]
ccn.pop(-1)

#Step 3 : Reverse the digits.
ccn.reverse()

#Step 4: Double every other element in the reversed list.
for i in range(0, len(ccn), 2):
    ccn[i] *= 2

#Step 5 : Subtract nine from numbers over nine.
for i in range(len(ccn)):
    if ccn[i] > 9:
        ccn[i] -= 9

#Step 6 : Sum all values.
total = 0
for x in ccn:
    total += x

#Step 7 : Take the second digit of that sum.
total = str(total)
# print(total)
if len(total) < 2: #if there is only one digit in the sum, it's the only one we can use
    second_digit = int(total[0])
else:
    second_digit = int(total[1])

#Step 8 : If that matches the check digit, the whole card number is valid.
if second_digit == check_digit:
    print("Valid!")
else:
    print("Invalid!")