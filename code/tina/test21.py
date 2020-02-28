jackelope_age = [0,0]

year = 0
age = 0

while len(jackelope_age) <= 1000:
  
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