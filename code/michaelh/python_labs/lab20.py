'''
# Lab 20: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
1. Convert the input string into a list of ints
2. Slice off the last digit.  That is the **check digit**.
3. Reverse the digits.
4. Double every other element in the reversed list.
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:
1. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5`
2. `4  5  5  6  7  3  7  5  8  6  8  9  9  8  5`
3. `5  8  9  9  8  6  8  5  7  3  7  6  5  5  4`
4. `10 8  18 9  16 6  16 5  14 3  14 6  10 5  8`
5. `1  8  9  9  7  6  7  5  5  3  5  6  1  5  8`
6. 85
7. 5
8. Valid!
'''
# credit = input('Enter a credit card number: ')
credit = '4556737586899855'
credit_list = []
for digit in credit:
    credit_list.append(int(digit))

# print(check_digit)
check_digit = credit_list.pop() #pop gets the last element by default
# print(check_digit)
credit_list.reverse()
# print(credit_list)
#Double every other element in the reversed list. For the other ones do nothing. Range and i are neccesary since the operation depends on the index.
credit_list_dub = [credit_list[i]*2 if i % 2 == 0 else credit_list[i] for i in range(len(credit_list))]
# print(credit_list_dub)
#Subtract nine from numbers over nine. Otherwise do nothing.
credit_list_sub = [digit - 9 if digit > 9 else digit for digit in credit_list_dub]
# print(credit_list_sub)
#Sum all values.
total = 0
for digit in credit_list_sub:
    total += int(digit)
print(str(total)[-1])
# print(total)
#Take the last digit of that sum. Convert total to a string so we can get the last digit. Then convert to an int to compare to check_digit.
if int(str(total)[-1]) == check_digit:
    print('Valid!')
else:
    print('Invalid!')
