first_dig_str = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

second_dig_str = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

teens_str = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
hundreds = []
[hundreds.append(str(second_dig_str[i]) + "-hundred") for i in range(len(second_dig_str))]

#print(hundreds)

user_number = input("Give me a number between 0-999: ")
user_num = []
[user_num.append(char) for char in user_number]
user_int = [int(num) for num in user_num]
user_int_copy = user_int.copy()
zero_digit = [user_int_copy.pop(0)]
teen_check = user_int_copy[0]

# print(user_num)
# print(user_int)
# print(user_int_copy)
# print(zero_digit)
# print(teen_check)

if len(zero_digit) == 1:
    for num in zero_digit:
        zero_dig = hundreds[num]
        break
    
if len(user_int) == 1:
    for num in user_int:
        if num == 0:
            first_dig = "zero"
        else:
            first_dig = second_dig_str[num]

elif len(user_int) > 1 and 9 < int(user_number) < 20:
    for num in user_int:
        first_dig = teens_str[num]

elif len(user_int) > 1 and int(user_number) > 20:
    for num in user_int:
        first_dig = first_dig_str[num]
        break
    second_dig = second_dig_str[user_int[1]]
    zero_dig = hundreds[user_int [0]]
else:
    pass

if len(user_int) > 2:
    for num in zero_digit:
        zero_dig = hundreds[num]
        break
    if teen_check == 1 and len(user_int_copy) == 2:
        for num in user_int_copy:
            first_dig = teens_str[num]
            print(first_dig)
    else:
        first_dig = first_dig_str[user_int[1]] 
        second_dig = second_dig_str[user_int[2]]
   

if len(user_int) > 2:
    if "00" in user_number:
        print(zero_dig)
    elif teen_check == 1 and len(user_int_copy) == 2:
        print(f"{zero_dig}-{first_dig}")
    else:
        print(f"{zero_dig}-{first_dig}-{second_dig}")
elif len(user_int) > 1 and 9 < int(user_number) < 20:
    print(first_dig)
elif len(user_int) > 1 and "0" in user_number:
    print(first_dig)
elif len(user_int) > 1:
    print(f"{first_dig}-{second_dig}")
else:
    pass


