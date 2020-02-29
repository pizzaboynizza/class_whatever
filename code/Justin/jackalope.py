# ## Jackelope Invasion ##
import random
# #Dies @ 10
# #Fertile (>=4-,<=8)
# #birth=2 per year/per every other jackelope
# #Goal=1000 Jackelopes
# #Print(Population has reached 1000 in {num} days)
year=0
jack=[{'name': 'Adam', 'gender': 'Male', 'age': 0, 'pregnant': False}, {'name': 'Eve', 'gender': 'Female', 'age': 0, 'pregnant': False}]
jack_per_age=0
total_pop=2
mort=0
gender=random.choice(['Male', 'Female'])
# generation=how many in each living generation
# print(gender)
# Change in Population Size = (births) vs. (deaths)
# while len(jack)<1000:
#     #Age of Jackelopes
#     for i in range(len(jack)):
#         jack[i] += 1
#     year += 1
#     #Count of Fertile
#     total_pop=0
#     for j in jack:
#         if j >=4 and j <=8:
#             total_pop += 1
#     total_pop = (total_pop//2)*2
def naming():
    name = ("Super", "Great", "Sexy", "Vegan", "Brave", "Shy", "Cool", "Poor", "Rich", "Fast", "Gummy", "Yummy", "Masked", "Unusual", "American", "Bisexual", "Lil","Coder", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "N00b","Son","Dottir","Jackelope","Facebook", "Science","Eksbok","MySpace")
    first = random.choice(name)
    total = (first)
    # if gender == 'Male':
    #     total+='son'
    # else:
    #     total+='sdottir'
    return(total)
#New Jackalopes
def njr():
    # {'name': naming(), 'gender':random.choice(['Male', 'Female']), 'age':0 ,'pregnant':False}
    return {'name': naming(), 'gender':random.choice(['Male', 'Female']), 'age':0 ,'pregnant':False}
while True:
    #Increment age
    for i in range(len(jack)):
        jack[i]['age'] += 1
    year += 1
# ​  #Give Birth
    for i in range(len(jack)):
        if jack[i]['pregnant']:
            jack[i]['pregnant'] = False
            jack.append(njr())
            jack.append(njr())

    #Murder
    num_kill = 0
    to_kill = []
    for i in range(len(jack)):
        if jack[i]['age'] >= 10:
            to_kill.append(i-num_kill)
            num_kill += 1
    for n in to_kill:
        jack.pop(n)
# ​
    #Shuffle List
    random.shuffle(jack)
# ​
    #Get Pregnant
    for i in range(len(jack)):
        if jack[i]['gender'] == 'Female' and jack[i]['age'] >= 4 and jack[i]['age'] <= 8 and jack[i]['pregnant'] == False:
            if jack[i-1]['gender'] == 'Male' and jack[i-1]['age'] >= 4 and jack[i-1]['age'] <= 8:
                jack[i]['pregnant'] = True
            elif i < (len(jack) - 1):
                if jack[i+1]['gender'] == 'Male' and jack[i+1]['age'] >= 4 and jack[i+1]['age'] <= 8:
                    jack[i]['pregnant'] = True
            elif jack[0]['gender'] == 'Male' and jack[0]['age'] >= 4 and jack[0]['age'] <= 8:
                jack[i]['pregnant'] = True
# ​
    input(jack)
# ​
#     #Reproduction
#     for i in range(total_pop):
#         jack.append(0)
# ​
# ​
#     #Mortality
#     try:
#         while True:
#             jack.remove(10)
#             mort +=1
#     except ValueError:
#         pass
# print(year)
# print(jack)
print(len(jack))
print(mort)
# print(naming())
# ​
print(njr())
# ​
# #Age
# #Gender
# #Pregnant(Who, Y/N)
# #Generate naming algorithm (0A-a)
# #Dies @ 10
# #Fertile (>=4-<=8)
# #birth=2 per year/per f j
# #Goal=1000 Jackelopes
# if {jack} == {age}:
#     if {jack} == <=4-<=8:
#         if {jack}==(female):
#             if {jack} == (fertile):
#                 <Birth*2>
#         if {jack}==(male):
#             <nothing>
# # num_death=
# num_preg=
# total_pop=
# time_pass=
# ​
# For Gender Randomization
# gender=random.choice(['Male', 'Female'])
# print(gender)



