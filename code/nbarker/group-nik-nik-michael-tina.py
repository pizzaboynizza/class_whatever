import random
print("Welcome to the Jackelope mating simulator!")

jack_lists = [{"name":"Adam", "age":0, "sex":"m", "preggo":False},{"name":"Eve", "age":0, "sex":"f", "preggo":False}]

fallen_jackelopes = []

while len(jack_lists) <= 10:

    for jackelope in jack_lists:
        jackelope["age"] += 1
        print(jack_lists)
        
    for i in range(len(jack_lists)):
        if jack_lists[i]["age"] == 10:
            del jack_lists[i]    
            
    # for jackelope in jack_lists:
    #     if jackelope["age"] >= 10:
    #         fallen_jackelopes.append(jackelope["name"])
    #         print(fallen_jackelopes)
    # for jackelope in jack_lists:
    #     if jack_lists["age"] == 10:
    #         remove(10)

'''
year = 0
age = 0

while len(jackelope_dictionary) <= 1000:
  
    num_births = 0

    for index in range(len(jackelope_age)):
        jackelope_age[index] += 1
        if 3 < jackelope_age[index] < 9 :
            num_births += 1

    # num_births = num_births//2

    while jackelope_age.count(10) > 0:
        jackelope_age.remove(10)

    for i in range(num_births):
        jackelope_age.append(0)
    
    print(jackelope_age)
    
    year += 1
else: 
    print("meow")
    print(year)

    '''