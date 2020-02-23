# Lab 10: Average Numbers
# We're going to average a list of numbers. 
nums = []
i = 0
# Start with the following list, iterate 
while i < 5:
    user_input = input("enter a number 1-10 or done if you would like to exit: ")
    if user_input != "done":
        int_num = int(user_input)
        nums.append(user_input)
        print(nums)
        i += 1
    elif user_input == "done":
        nums = [int(i) for i in nums]
        average = sum(nums) / len(nums)
        print(average)
else:
        nums = [int(i) for i in nums]
        average = sum(nums) / len(nums)
        print(average)
    

# through it, keeping a 'running sum', then 
# divide that sum by the number of elements
#  in that list. Remember len will give you the length of a list.

# The code below hows how to loop through an array, 
# and prints the elements one at a time.

# nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# for num in nums:
#     print(num)

# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])
# Version 2
# Ask the user to enter the numbers one at a time, 
# putting them into a list. If the user enters 'done',
#  then calculate and display the average. 
# The following code demonstrates how to add an
#  element to the end of a list.

# nums = []
# nums.append(5)
# print(nums)
# Below is an example input/output:

# > enter a number, or 'done': 5
# > enter a number, or 'done': 3
# > enter a number, or 'done': 4
# > enter a number, or 'done': done
# average: 4
