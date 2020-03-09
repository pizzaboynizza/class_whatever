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
    print(nums[i])'''
#VERSION 1
nums = [5, 0, 8, 3, 4, 1, 6]
# i'm going to need a for loop to iterate the list
# im going to need a variable(total) thats adds to the list
sum = 0
for i in nums:
    sum+=i 
print(sum)
new_sum = sum/len(nums)
print(round(new_sum,2))


#VERSION 2
nums = []
sum = 0
while True:
  user = input("Enter number or done: ")
  if user == 'done':
    break
  nums.append(int(user))
print(nums)
for i in nums:
  sum+=i
average = sum/len(nums)
print(f"The Average of {nums} is {average}")


