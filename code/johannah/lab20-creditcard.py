'''
1. Convert the input string into a list of ints
2. Slice off the last digit. That is the check digit.
3. Reverse the digits.
4. Double every other element in the reversed list.
5. Subtract nine from numbers over nine.
6. Sum all values.
7. Take the second digit of that sum.
8. If that matches the check digit, the whole card number is valid.
'''

nums = []
while True:
  user_input = input("Enter your credit card number one number at a time and then press a blank enter when complete: ")
  if user_input:
    nums.append(int(user_input))
  else:
    break
print(nums)
# 2. Slice off the last digit. That is the check digit
nums_sliced = nums[0:-1]
print(nums_sliced)
# 3. Reverse the digits
nums_reversed = nums_sliced[::-1]
print(nums_reversed)
# 4. Double every other element in the reversed list
for i in range(0,len(nums_reversed),2):
    nums_reversed[i] *= 2
print(nums_reversed)
# 5. Subtract nine from numbers over nine.
for i in range(len(nums_reversed)):
    if nums_reversed[i] > 9:
        nums_reversed[i] -= 9
print(nums_reversed)
# 6. Sum all values
sum_vals = sum(nums_reversed)
print(sum_vals)
# 7. Take the second digit of that sum.
string_sum = str(sum_vals)
second_digit = string_sum[1]
print(second_digit)
# 8. If that matches the check digit (the last digit from step 1), the whole card number is valid
check_digit = str(nums[-1])
# print(type(check_digit))
# print(type(second_digit))
if second_digit == check_digit:
    print("Valid!")
else:
    print("Sorry that is invalid.")