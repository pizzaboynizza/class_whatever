with open('contact-list.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)
    print(lines[0])  # Name,Email,Favorite Color
    # print(type(lines))  # lines is a LIST of strings
    # print(type(lines[0])) # lines at any index is a STRING

"""
-extract each row/line from csv and bring to python
    -index 0 IS the key for each row/line
-append to dict
"""

#keys = []

line_zero = lines[0].split(',')  # key for each 
line_one = lines[1].split(',')
line_two = lines[2].split(',')   # THESE ARE ALL STRINGS
line_three = lines[3].split(',')
line_four = lines[4].split(',')
# contact_list = {line_one, line_two, line_three, line_four}
# print(contact_list)
# print(line_zero[0])
# print(line_one[1])
# print(line_two[2])
# print(line_three[0])
# print(line_four[1])
key_one = line_zero[0]
key_two = line_zero[1]
key_three = line_zero[2]
# print(key_one)
# print(key_two)
# print(key_three)
print(line_one)



# contact_list = []
# for line in lines:
#     contact_list.append(line)
#     print(contact_list)

# contact_list = {}
# print(contact_list[lines])
# for line in lines:
#     contact_list.append(line)
#     print(contact_list)


# contact_list = [
#     {'name':'jane', 'email':'jane@company.net', 'favorite color':'red'},
#     {'name':'bob', 'email':'bob@company.net', 'favorite color':'blue'},
#     {'name':'jack', 'email':'jack@company.net', 'favorite color':'silver'},
#     {'name':'diana', 'email':'diana@company.net', 'favorite color':'yellow'}
# ]

'''
end result
'''
# contact_list = [
#     {key_one:line_one[0], key_two:line_one[1], key_three:line_one[2]},
#     {key_one:line_two[0], key_two:line_two[1], key_three:line_two[2]},
#     {key_one:line_three[0], key_two:line_three[1], key_three:line_three[2]},
#     {key_one:line_four[0], key_two:line_four[1], key_three:line_four[2]}
# ]

'''
how to create dictionaries inside a list
'''