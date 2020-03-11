with open('contacts.csv', 'r') as file:
    lines = file.read()
    # print(lines)
lines = lines.split( '\n') #spliting into a list of lines
# print(lines)

keys = lines[0].split(',')
print(keys)