'''

Lab 10: Average Numbers
job:We're going to average a list of numbers. 
Instructions
1)Start with the following list, 
2)terate through it, 
3) keeping a 'running sum', 
4)then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below hows how to loop through an array, and prints the elements one at a time.

nums = [5, 0, 8, 3, 4, 1, 6]

# loop over the elements
for num in nums:
    print(num)

# loop over the indices
for i in range(len(nums)):
    print(nums[i])

'''
nums = []
total = 0
while True:
    user_input = input("Enter number or done: ")
    if user_input == 'done':
        break
    nums.append(int(user_input))
print(nums)

for numbers in nums:
    total+= numbers
new_total = total/len(nums)
print(f"Average is {new_total}")



