nums = [5, 0, 8, 3, 4, 1, 6]

total = 0
for x in nums:
    total += int(x)
# print(total,'this is x')


while True:
    user = input('enter a number or type done: ')
    nums.append(user)
    if user in ['done']:
        print(nums)
        break

    
Ave = total / len(nums)
print(Ave)
    




 