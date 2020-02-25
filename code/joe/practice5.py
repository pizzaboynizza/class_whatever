# Practice 5
# Author : Joe
import string

prob1 = [2**i for i in range(10)]

prob2 = [i for i in range(2, 21, 2)]

dict1 = {"a" : 1, "b" : 2, "c" : 3}

prob3 = {num: let for let, num in dict1.items()}

prob4 = {let: ord(let) for let in string.ascii_lowercase}


print(f"First 10 powers of 2:\n{prob1}\n")

print(f"First 10 even numbers:\n{prob2}\n")

print(f"Swap keys and values of {dict1}:\n{prob3}\n")

print(f"Each letter of the alphabet and corrisponding ascii value:\n{prob4}\n")