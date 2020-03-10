# def inputs():
#     thing_one = input("Type something: \n")
#     thing_two = input("And something else: ")
#     if thing_one == thing_two:
#         print("They are equal")
#     else:
#         print("Those are not equal.")
# inputs()


# thing_one = input("Enter a thing: ")
# thing_two = input("Enter a thing2: ")
# thing_three = input("Enter a thing3: ")

# if thing_one == thing_two == thing_three:
#     print("yes!")
# elif thing_one == thing_two or thing_one == thing_three or thing_two == thing_three:
#     print("Some are indeed equal")
# else:
#     print("Nope...")

# num1 = int(input("Pick a number: "))
# num2 = int(input("Pick another number: "))
# sum = num1 + num2
# if sum == 5:
#     print("5!")
# elif sum <5:
#     print("Less than 5!")
# else:
#     print("Greater than 5!")

# grade_input = int(input("Enter your test score: "))

# passing_grade = 35

# if grade_input > passing_grade:
#     print("Good work!")
# elif grade_input == 35:
#     print("you barely made it!")
# else:
#     print("u failed")

# length = int(input("What's the length of your rectangle in cm? "))
# width = int(input("What's the width of your rectangle in cm? "))

# if length == width:
#     print("squared!")
# else:
#     print("tis a retangle(not a square)!")

# one = int(input("Input one? "))
# two = int(input("input two? "))

# if one > two:
#     print(one)
# elif one == two:
#     print("those are actually equal....")
# else:
#     print(two)

# items = int(input("How many $100 items would you like to buy? "))

# price = (items * 100)
# if price >= 1000:
#     price_if_greater_than_1000 = (items * 100) * .10
#     total_price = price - price_if_greater_than_1000
#     print(f"here is a discount of ${price_if_greater_than_1000} your total will be: ${total_price}.")
# else:
#     print(f"your items will cost ${price}.")

# salary = int(input("How much did you make this year? $"))
# tenure = int(input("How many years have you been with the company? "))

# if tenure >= 5:
#     bonus = salary * .05
#     salary_plus_bonus = bonus + salary
#     salary_plus_bonus = int(salary_plus_bonus)
#     print(f"Congrates on being with us for 5+ years! Here is a ${bonus}!!!")
# else:
#     print("Sorry, no bonus for you, bro!")

# age1 = int(input("How old are you? "))
# age2 = int(input("How old are you? "))
# age3 = int(input("How old are you? "))

# age_sorted = sorted([age1, age2, age3])

# if age1 > age2 and age1 > age3:
#     print(f"the oldest is {age1} the second oldest is {age2} and the third is {age3}")
# elif age2 > age3 and age1 > age3:
#     print(f"the oldest is {age2}, the second oldest is {age1} and the third is {age3}")
# elif age3 > age2 and age3 
# else:
#     print(f"they are all even}")

# number = int(input("enter the number for an absolute value. "))

# if number < 0:
#     number2 = number * -1
#     print(f"The absolute value of the number is {number2}.")
# else:
#     print(f"The absolute value of the number is {number}.")

# classes_held = int(input("How many classes have occurred? "))
# attendance = int(input("How many classes have you attended? "))

# percentage_of_Attendance = (attendance / classes_held) * 100

# print(f"percentage of attendance: {percentage_of_Attendance}")

# if percentage_of_Attendance >= 75:
#     print("You may take the exam!")
# elif percentage_of_Attendance <= 74:
#     print("You shouldn't have skipped.... no exam for you!")
#     medical_excuse = input("Do you have a doctor's note? ")
#     if medical_excuse == "yes":
#         print("Okay, we'll allow you to take the exam.")

# random_list = [1,6878945,506949,458993,395,61,8,9,0,]

# for item in random_list:
#     print(item)

# random_list = []
# for x in range(0, 4):
#     random_list_input = input("user enter a list, when finished write done: ")
#     random_list.append(random_list_input)
#     print(random_list)

# user_input = input("What element would you like to delete: ")

# if user_input in random_list:
#     random_list.remove(user_input)
# else:
#     print("That's not in the list!")

# print(random_list)

lst = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

print 


'''
Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.
'''