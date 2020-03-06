"""
Mob Programming: Jackalope Simulator
Version 1
The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

Jackalopes are reproductive from ages 4-8 and die at age 10.
Gestation is instantaneous. Each gestation produces two offspring.
Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do
With these conditions in mind, we can represent our population as a list of ints.
"""

count_population = []
count_reproductive = []
num_yearsTaken = 0


#jackalope and age will be equal for version 1 (defining jackalope as its age)


jack = [0, 0]
years = 0

while len(jack) <= 1000:
    
    for i in range(0, len(jack)):
        # if jack >= 3 and jack <= 7:
        if 3 <= jack[i] <= 7:
            jack[i] += 1
            jack.append(0)
            print(jack)
        elif jack[i] > 9:
            jack.remove(jack[i])
        else:
            jack[i] += 1
            print(jack)
    years += 1
# for i in range(0, len(jack)):
#     if jack[i] == 10:
#         jack.remove(10)
    
print(jack)
print(len(jack))
print(years)

    # for i in range(0, len(jack)):
    #     while jack[i] >= 10:
    #         jack.remove(jack[i])
    #         print(jack)
    #     else:
    #         if 10 not in range(len(jack)):
    #             print("nope")


# jackalope = []


# my_list = [0, 0]

# for age in my_list:
#     if 4 <= age <= 8:
#         age += 1
#         # my_list.append(0) * 2
#     elif age < 4:
#         age += 1
#     print(age)
#     print(my_list)
    # else:
    #     age += 1
    #     if age == 10:
    #         my_list.remove()






# age = 0

# reproductive = []
# #     if 

# startPop = 2

# for jackalope/2 in population:
#     if 4 <= age <= 8:
#         population += 2

# for jackalope in population:
#     if age == 10:
#         population -= 1

# if population == 1000:
#     print("done")
# #     break


# population_end = 1000

# population = 2
# year = 0

# for population / 2:
#     population * 16

# year += 1