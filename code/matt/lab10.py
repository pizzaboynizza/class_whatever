"""
Lab 10: Average Numbers
Version 1
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 
'running sum', then divide that sum by the number of elements in that list. 

Version 1 code:
counter = 0
nums = [5, 0, 8, 3, 4, 1, 6]
# add_nums = [num for num in nums counter+=]

for num in nums:
    counter += num
print(counter / len(nums))

Version 2
Ask the user to enter the numbers one at a time, putting them into a list. 
If the user enters 'done', then calculate and display the average. 
Version 2 code:
"""
import string

user_num = []
counter = 0
while True:
    user_in = input("Enter a number or \'done\': ")
    if user_in == "done":
        if len(user_num) > 0:
            for num in user_num:
                counter += int(num)
            avg_num = counter / len(user_num)
            print(f"{user_num} average is {avg_num}.")
        print("Goodbye.")
        break
    elif user_in not in string.digits:
        print("Must be a number")
    else:
        user_num.append(user_in)