nums = []

print("Let's find the average of a list of numbers!")

user_input = input("give me a number!\n>")
if user_input.isnumeric() == True:
    user_input = int(user_input)
else:
    print("Invalid entry. Sorry!")
    quit()


while isinstance(user_input, int) == True:
    nums.append(user_input)
    user_input = input("give me a number, or type 'done'\n>")
    if user_input == "done":
        break
    else:
        user_input = int(user_input)
        continue

total = 0 

for i in range(len(nums)):
    total = total + nums[i]
average = total/len(nums)
average = round(average, 2)
print(f"The average of your numbers is {average}")
