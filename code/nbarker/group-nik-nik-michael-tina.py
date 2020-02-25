import math
print("Welcome to the Jackelope Sex Calculator 5000!")



jackelope_age = [0,0]

year = 0
age = 0
while len(jackelope_age) <= 15:
    killed_jackelopes = []
    num_births = 0
    for index in range(len(jackelope_age)):
        jackelope_age[index] += 1
        if jackelope_age[index] >= 10:
            killed_jackelopes.append(index)
        if 4 < jackelope_age[index] < 9 :
            num_births += 1
    num_births = num_births//2
    for death in killed_jackelopes:
        jackelope_age.pop(death)
    for i in range(num_births):
        jackelope_age.append(0)
    print(jackelope_age)
    year += 1
else: 
    print("meow")
    print(year)