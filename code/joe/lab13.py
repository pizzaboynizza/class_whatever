# Lab 13
# Author : Joe

def rot_n(char, rotate):
    temp = ord(char)
    if char.isalpha():
        temp -= 64 if char.isupper() else 96
        temp = (temp + rotate) % 26
        temp += 64 if char.isupper() else 96
    return chr(temp)

word = input("Enter string: ")

to_rot = input("Enter amount to rotate: ")
while not to_rot.isdigit():
    to_rot = input("Must enter a number: ")
to_rot = int(to_rot)

conv = ""
for i in range(len(word)):
    conv += rot_n(word[i], to_rot)

print("Encrypted text:\n\t", conv)