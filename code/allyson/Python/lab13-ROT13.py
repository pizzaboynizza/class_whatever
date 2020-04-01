from string import ascii_lowercase

input_string=input('Input Message:  ').lower()
# ROT=string.ascii_lowercase
def rotate(input_string, ROT):
    cipher = list()
    for char in input_string:
        if char.lower() in ascii_lowercase:
            index = (ascii_lowercase.find(char.lower()) + ROT) - (int((ascii_lowercase.find(char.lower()) + ROT) / 26) * 26)
            cipher.append(ascii_lowercase[index]) if char.islower() else cipher.append(ascii_lowercase[index].upper())
        else:
            cipher.append(char)
    return ''.join(cipher)
print(rotate(input_string,13))