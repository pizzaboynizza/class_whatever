
import random

year=0
jack=[{'name': 'Adam', 'gender': 'Male', 'age': 0, 'pregnant': False}, {'name': 'Eve', 'gender': 'Female', 'age': 0, 'pregnant': False}]
jack_per_age=0
total_pop=2
gender=random.choice(['Male', 'Female'])
​
def naming():
    name = ("Super", "Great", "Sexy", "Vegan", "Brave", "Shy", "Cool", "Poor", "Rich", "Fast", "Gummy", "Yummy", "Masked", "Unusual", "American", "Bisexual", "Lil","Coder", "Vegan", "Man", "Hacker", "Horse", "Bear", "Goat", "Goblin", "Learner", "Killer", "Woman", "Programmer", "Spy", "Stalker", "Spooderman", "Carrot", "Goat", "Quickscoper", "N00b","Son","Dottir","Jackelope","Facebook", "Science","Eksbok","MySpace")
    first = random.choice(name)
    total = first
​
    return(total)
​
    # {'name': naming(), 'gender':random.choice(['Male', 'Female']), 'age':0 ,'pregnant':False}
    return {'name': naming(), 'gender':random.choice(['Male', 'Female']), 'age':0 ,'pregnant':False}
​
while True:
    #Increment age
    for i in range(len(jack)):
        jack[i]['age'] += 1
    year += 1
​
    #Give Birth
    for i in range(len(jack)):
        if jack[i]['pregnant']:
            jack[i]['pregnant'] = False
            jack.append(njr())
            jack.append(njr())
​
    num_kill = 0
    to_kill = []
    for i in range(len(jack)):
        if jack[i]['age'] >= 10:
            to_kill.append(i-num_kill)
            num_kill += 1
    for n in to_kill:
        jack.pop(n)
​
    random.shuffle(jack)
​
    for i in range(len(jack)):
        if jack[i]['gender'] == 'Female' and jack[i]['age'] >= 4 and jack[i]['age'] <= 8 and jack[i]['pregnant'] == False:
            if jack[i-1]['gender'] == 'Male' and jack[i-1]['age'] >= 4 and jack[i-1]['age'] <= 8:
                jack[i]['pregnant'] = True
            elif i < (len(jack) - 1):
                if jack[i+1]['gender'] == 'Male' and jack[i+1]['age'] >= 4 and jack[i+1]['age'] <= 8:
                    jack[i]['pregnant'] = True
            elif jack[0]['gender'] == 'Male' and jack[0]['age'] >= 4 and jack[0]['age'] <= 8:
                jack[i]['pregnant'] = True
​
    input(jack)
​
print(len(jack))
print(mort)

​
print(njr())
​