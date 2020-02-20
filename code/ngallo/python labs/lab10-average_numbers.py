nums = []

while True:
    user_number = input('enter a number, or done ')
    if user_number == 'done':
        print(mean)
        break
    else:
        nums.append(int(user_number))
        answer = sum(nums)
        mean = (answer / 2)