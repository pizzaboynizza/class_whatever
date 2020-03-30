'''Lab 20: Credit Card Validation
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:

Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:

4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!
'''

# credit_numbers = []
# while True:
#     user_input = input(" Enter card numbers or done: ")
#     if user_input == 'done':
#         break
#     credit_numbers.append(int(user_input))
# # print(credit_numbers)
# credit_numbers.pop(-1)
# # print(credit_numbers)
# # print(list(reversed(credit_numbers)))
# credit_numbers = [x**2 for x in len(range(::2))]
# print(credit_numbers)

user_input = input(" Enter card numbers: ")
# turn that user input into a list of numbers by iterating thought
credit_numbers = [int(x) for x in str(user_input)]
print(credit_numbers)
# pop off the last number in the list
credit_numbers.pop()
print(credit_numbers)
# reverse the card numbers
credit_numbers.reverse()
print(credit_numbers)
# multiply the numbers by 2 if they are even numbers aka every other number
new_list = [2 * n if i % 2 == 0 else n for i, n in enumerate(credit_numbers)]
print(new_list)
for number in range(len(new_list)):
    if new_list[number] > 9:
        new_list[number] -= 9
print(new_list)
total = 0
for numbers in new_list:
    total+= numbers
print(total)
new_total = total%10
print(new_total)




#append the numbers into a list

#do a comprehension(Double everyother no.) of the list in reverse



