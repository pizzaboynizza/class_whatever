'''
Nick Barker
Lab 10
Average Numbers
2/20/2020
'''

#average a list of numbers **nums = [5, 0, 8, 3, 4, 1, 6]**
#iterate through it, keeping a running sum
#then divide that sum by the number of elements in that list
#remember len will give you the length of a list


print("Let's hope this number averager is above average")

#keeping a running sum
runsum = sum(nums)
print(runsum)

#divide that sum by the number of elementts
avg = runsum/len(nums)
print(avg)

Ask the user to enter the numbers one at a time, putting them into a list. If the user enters 'done', then calculate and display the average. The following code demonstrates how to add an element to the end of a list.

nums = []
i = 0

while i < 5:

    num = input("Please enter a number between 1 and 100, or boner if you would like an average of your previously entered numbers ")
    if num != "boner":
        int_num = int(num)
        nums.append(num)
        print(nums)
        i += 1
    elif num == "boner":
        nums = [int(i) for i in nums]
        average = sum(nums)/len(nums)
        print(int(average))
    else: print("error")
else:
    nums = [int(i) for i in nums]
    average = sum(nums)/len(nums)
    print(int(average))
    #the end