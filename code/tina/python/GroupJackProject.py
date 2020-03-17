import random
import string
def can_get_preggers(jackelope):
    print(jackelope)
    if 3 < jackelope["age"] < 9 and jackelope["sex"] == "f" and jackelope["preggo"] == False:
        return True
    else:
        return False
    #make sure female
    #is already preggers

def make_new_jackelope():
    list_vowels = ["a", "e", "i", "o", "u", "y"]
    # list_alphabet = string.ascii_lowercase
    list_constanants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
    name = random.choice(list_constanants) + random.choice(list_vowels) + random.choice(list_constanants)
    age = 0
    sex = random.choice(["m","f"])
    preggo = False
    return {"name":name, "age":age, "sex":sex, "preggo":preggo}

print("Welcome to the Jackelope mating simulator!")

jack_lists = [{"name":"Adam", "age":0, "sex":"m", "preggo":False},{"name":"Eve", "age":0, "sex":"f", "preggo":False}]

fallen_jackelopes = []


while len(jack_lists) <= 30:

    #increase age
    for jackelope in jack_lists:
        jackelope["age"] += 1
        # print(jack_lists)
        
    # remove if too old
    for i in range(len(jack_lists)):
        if jack_lists[i]["age"] == 10:
            jack_lists.remove(i)


    #making preggo
    for j in range(len(jack_lists)):
        # print(can_get_preggers(jack_lists[j]))
        # print(jack_lists[j-1]["sex"])
        # print(jack_lists[j+1]["sex"])
        if can_get_preggers(jack_lists[j]) and (jack_lists[j-1]["sex"] == "m" or jack_lists[j+1]["sex"] == "m"):
            if can_get_preggers(jack_lists[j]):
                jack_lists[j]["preggo"] = True
 
    #counting births
    num_births = 0
    for jackelope in jack_lists:
        if jackelope["preggo"] == True:
            num_births += 1
            jackelope["preggo"] == False
    print(num_births)


    new_jackelope = {}
    for i in range(num_births):
        # print("Im here")
        new_jackelope = make_new_jackelope()
        jack_lists.append(new_jackelope) 
        
    for jackelope in jack_lists:
        if jackelope["age"] >= 10:
            fallen_jackelopes.append(jackelope["name"])
            print("this is fallen Jack", fallen_jackelopes)
    #
    # 
    #  for jackelope in jack_lists:
    #     if jack_lists["age"] == 10:
    #         jack_lists.remove(10)

print(jack_lists)

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