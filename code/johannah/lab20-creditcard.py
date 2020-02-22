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


'''
nums = []
while True:
  user_input = input("Enter your credit card number one number at a time and then enter \'done\' when complete: ")
  if user_input == a number:
    continue
  elif user_input == "done":
    break
    print(nums.append(float(user_input)))
'''

nums = []
while True:
    user_input = input("Enter your credit card number one number at a time and then press a blank enter when complete: ")
    if user_input:
        nums.append(user_input)
    else:
        break
print(nums)

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


'''
user_input = input('Type here: ')
nums = [user_input]


magicInput = input('Type here: ')
magicList = list(magicInput)
print(magicList)
'''