nums = []
while True:
  user_input = input("Enter each number one at a time and then type \'done\' when complete: ")
  if user_input == "done":
    break
  else:
    nums.append(float(user_input))

total = 0
for num in nums:
  total += num
average = total/len(nums)
print("The average is: " + str(average))