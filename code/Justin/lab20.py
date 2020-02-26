credit_card_number = [8,4,7,3,2,5,2,3,8,4,5,8,2,3,7,4]

for nums in credit_card_number:
    nums = int(nums)

credit_card_number.pop()

credit_card_number.reverse()

numbers = credit_card_number

l = numbers[:]
l[::2] = [x*2 for x in l[::2]]

l2 = []
total = 0
for n in l:
    if n > 9:
        l2.append(n-9)
        total += (n - 9)

    else:
        l2.append(n)
        total += n

    l3 = sum(l2)

final = total%10

print(final)

print("invalid!")







