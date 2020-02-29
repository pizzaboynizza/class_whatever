jack = [0, 0]
years = 0
while len(jack) <= 1000:
    for i in range(len(jack)-1, -1, -1):
        jack[i] += 1
        if 3 < jack[i] < 9:
            jack.append(0)
        elif jack[i] == 10:
            jack.remove(jack[i])
    years += 1
        
population = len(jack) 
print(jack)
print(population)
print(years)
    
        
        
'''
Version 2

Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. A jackalope will have the following properties:

name
age
sex
whether they're pregnant
Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.
'''