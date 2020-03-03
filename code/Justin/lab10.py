
nums = [5, 0, 8, 3, 4, 1, 6]

total = 0
for num in nums:
    total += num

print(total/len(nums))

nums2 = []

while True:

    user_input = input("pick a number:")

    nums2.append(user_input)
    print(nums2)

    if user_input == "done":

        nums2.pop()
        print(nums2)

        #nums2 = int(nums2)
        print(nums2)

        for num in range(0, len(nums2)):
            nums2[num] = int(nums2[num])
        print(str(nums2))

        answer = sum(nums2)/len(nums2)
        print(answer)
        break







