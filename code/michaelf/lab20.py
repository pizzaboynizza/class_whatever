user_input = input("Give me your credit card number: ")
user_input = user_input.strip()

if user_input.isnumeric() == True:
    pass
else:
    print("Invalid entry. Sorry!")
    quit()

user_list = []
[user_list.append(char) for char in user_input]
user_list_check = user_list.pop(-1)
#print(user_list)
user_list.reverse()
user_list = [int(element) for element in user_list]
#print(user_list)


user_list_dbl = [user_list[i] * 2 if i % 2 == 0 else user_list[i] for i in range(len(user_list))]

user_list_subtract = [num - 9 if num > 9 else num for num in user_list_dbl]


#print(user_list)
#print(user_list_dbl)
#print(user_list_subtract)
total = 0 
for i in range(len(user_list_subtract)):
    total = total + user_list_subtract[i] 
#print(total)

total = str(total)
second_digit = total[1]
#print(second_digit)

if second_digit == user_list_check:
    print("Valid!")
else:
    print("Invalid! Sorry!")

# abandoned below, looking into reduce as we speak
# user_list_sum = [user_list_subtract[i] + total for i in range(len(user_list_subtract))]
# print(user_list_sum)
