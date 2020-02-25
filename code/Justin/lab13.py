
def rot_Cipher(user_input):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""

    for i in user_input:
        output += alphabet[(alphabet.find(i) + 13) % 26]
    return output

print(rot_Cipher("justin"))