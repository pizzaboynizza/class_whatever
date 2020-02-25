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
#print(nums.append(float(user_input)))
print(nums)
nums_sliced = nums[0:-1]
print(nums_sliced)
nums_reversed = nums_sliced[::-1]
print(nums_reversed)
# 4. Double every other element in the reversed list
double_second = (nums_reversed[0::2])*2
#[0:-1:2]
#[x*2 for x in range(10)]
print(double_second)

'''
items=[]
i=0
while 1:
    i+=1
    item=input('Enter item %d: '%i)
    if item=='':
        break
    items.append(item)
print(items)
'''