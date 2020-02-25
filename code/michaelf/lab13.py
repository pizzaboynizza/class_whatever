import string

def rot13():
    phrase = input("Give me a phrase to encode: ").casefold()
    phrase = list(phrase[::])
    rot = int(input("Give me the number of rotation you'd like for your encryption: "))

    english = list(string.ascii_lowercase)
    encode = list(string.ascii_lowercase)
    # english_dict = dict(zip(english, encode))
    encode_dict = {english[i]: encode[i-rot] for i in range(0, 26)}
    encode_dict.update({' ' : ' ', '!':'!', '.': '.', ',' : ','})
    encoded = [encode_dict[char] for char in phrase]
    encoded = ''.join(encoded)
    print(encoded)

rot13()