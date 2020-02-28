import random
import string
def can_get_preggers(jackelope):
    if 3 < jackelope["age"] < 9 and jackelope["sex"] == "f" and jackelope["preggo"] == False:
        return True
    else:
        return False
    #make sure female
    #is already preggers

def make_new_jackelope():
    list_vowels = ["a", "e", "i", "o", "u", "y"]
    list_constanants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
    name = random.choice(list_constanants).upper() + random.choice(list_vowels) + random.choice(list_constanants)
    age = 0
    sex = random.choice(["m","f"])
    preggo = False
    return {"name":name, "age":age, "sex":sex, "preggo":preggo}

#This function returns True if there is a jackelope that is age 10 in the list and otherwise returns False
def kill_jackelopes(jack_lists):
    oldest = 0
    for jackelope in jack_lists:
        if jackelope["age"] > oldest:
            oldest = jackelope["age"]
    if oldest == 10:
        return True
    else:
        return False

#This function returns the index of the first jackelope that is age 10
def get_first_old_jackelope_index(jacks_list):
    for i in range(len(jacks_list)):
        if jack_lists[i]["age"] == 10:
            return i

jack_lists = [{"name":"Adam", "age":0, "sex":"m", "preggo":False},{"name":"Eve", "age":0, "sex":"f", "preggo":False}]
year = 0
while 1 < len(jack_lists) < 1000:
    year += 1
    #increase age
    for jackelope in jack_lists:
        jackelope["age"] += 1
    
    #counting births
    num_births = 0
    for jackelope in jack_lists:
        if jackelope["preggo"]:
            num_births += 1
            jackelope["preggo"] = False
    new_jackelope = {}
    for i in range(num_births):
        new_jackelope = make_new_jackelope()
        jack_lists.append(new_jackelope)

    #making preggo
    #these first two conditions handle the first and last elements of jack_list they are special cases since they just have one jackelope nearby
    if can_get_preggers(jack_lists[0]) and jack_lists[1]["sex"] == "m":
        jack_lists[0]["preggo"] = True
    elif can_get_preggers(jack_lists[len(jack_lists) - 1]) and jack_lists[len(jack_lists) - 2]["sex"] == "m":
        jack_lists[len(jack_lists) - 1]["preggo"] = True    
    #this is for the rest of those pesky jackelopes (those that have two neighbors)
    for j in range(1,len(jack_lists)-1):
        if can_get_preggers(jack_lists[j]) and (jack_lists[j-1]["sex"] == "m" or jack_lists[j+1]["sex"] == "m"):
        # if can_get_preggers(jack_lists[j]):
            jack_lists[j]["preggo"] = True
            # print("here I am")

    while kill_jackelopes(jack_lists):
        jack_lists.pop(get_first_old_jackelope_index(jack_lists))
    random.shuffle(jack_lists)
    print(f"The year is {year} and there are {len(jack_lists)} jackelopes.")

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