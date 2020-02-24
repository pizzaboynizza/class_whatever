first_dig_str = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

second_dig_str = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

teens_str = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

user_number = input("Give me a number between 0-99: ")
user_num = []
[user_num.append(char) for char in user_number]
user_int = [int(num) for num in user_num]

# print(user_num)
# print(user_int)

if len(user_int) > 1 and int(user_number) > 19:
    for num in user_int:
        first_dig = first_dig_str[num]
        break
    second_dig = second_dig_str[user_int[1]]

if len(user_int) > 1 and 9 < int(user_number) < 20:
    for num in user_int:
        teens = teens_str[num]
    

if len(user_int) == 1:
    for num in user_int:
        if num == 0:
            first_dig = "zero"
        else:
            first_dig = second_dig_str[num]

if len(user_int) > 1 and 9 < int(user_number) < 20:
    print(teens)
elif len(user_int) > 1 and "0" in user_number:
    print(first_dig)
elif len(user_int) > 1:
    print(f"{first_dig}-{second_dig}")
else:
    pass


