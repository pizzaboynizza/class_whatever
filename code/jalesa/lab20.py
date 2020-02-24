# Lab 20: Credit Card Validation
# Let's write a function which returns whether
#  a string containing a credit card number is
#  valid as a boolean. The steps are as follows:

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


card_number = input("Enter your 16 digit credit card number: ")
new_card_number = list(map(int,card_number))
# print(new_card_number)

check_digit = new_card_number.pop(-1)
# print(last_number)


new_card_number.reverse()
# print(new_card_number)


everyother_element = enumerate(new_card_number)
# print(list(everyother_element))   
# if i print list i get 
# empty list for new_one

# Double every other element in the reversed list.
new_one = [n * 2 if i % 2 == 0 else n for i,n in everyother_element] 
print(new_one)

# Subtract nine from numbers over nine.
subtract_nine = [n - 9 if n > 9 else n for n in new_one]
print(subtract_nine)

# Sum all values.
sum_of_values = sum(subtract_nine)
print(sum_of_values)

# Take the second digit of that sum.
second_digit = sum_of_values % 10
print(second_digit)


# If that matches the check digit, the whole card number is valid.
check_digit == second_digit
print("card number is valid.")


