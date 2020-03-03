# first_dig_str = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

# second_dig_str = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

# teens_str = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
# hundreds = []
# [hundreds.append(str(second_dig_str[i]) + "-hundred") for i in range(len(second_dig_str))]

roman_ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
roman_tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
roman_hundreds = ['','C','CC','CCC','CD','D','DC','DCC','DCCC', 'CM']


user_number = input("Give me a number between 0-999: ")
user_num = []
[user_num.append(char) for char in user_number]
user_int = [int(num) for num in user_num]
print(user_int)
user_int_copy = user_int.copy()
zero_digit = [user_int_copy.pop(0)]
# teen_check = user_int_copy[0]


    
if len(user_int) == 1:
    ones_dig = roman_ones[user_int[0]]
    tens_dig = ''
    hundreds_dig = ''

elif len(user_int) == 2:
    ones_dig = roman_ones[user_int[1]]
    tens_dig = roman_tens[user_int[0]]
    hundreds_dig = ''

elif len(user_int) == 3:
    hundreds_dig = roman_hundreds[user_int[0]]
    tens_dig = roman_tens[user_int[1]] 
    ones_dig = roman_ones[user_int[2]]
   


if "00" in user_number:
    print(hundreds_dig)
elif len(user_int) == 2 and "0" in user_number:
    print(tens_dig)
else:
    print(f"{hundreds_dig}{tens_dig}{ones_dig}")


