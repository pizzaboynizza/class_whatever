#Lab 10
#Author : Joe

nums = []

while True:
    user_in = input("Please enter a number or 'done': ")
    if user_in == "done":
        if len(nums) == 0:
            print("Must enter at least one number!") #prevent dividing by zero errors
        else:
            break
    else:
        try: #ensure a number was entered
            user_in = float(user_in)
            nums.append(user_in)
        except ValueError:
            print("Invalid input!")


sum = 0

for num in nums:
    sum += num

print(f"The average of {nums} is {sum/len(nums)}")