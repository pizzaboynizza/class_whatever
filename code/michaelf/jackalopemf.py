jack = [0, 0]
years = 0
population = len(jack)

# check = list(range(len(jack)-1))
# print(check)
while len(jack) <= 1000: 
    for i in range(len(jack)-1, -1, -1):
        if 0 <= jack[i] < 4:
            jack[i] += 1
            # if jack == 10:
            #     jack.remove(jack[i])
        
        elif 4 <= jack[i] <= 8:
            jack[i] += 1
            jack.append(0)
            # if jack == 10:
            #     jack.remove(jack[i])
            
        else:
            pass
            # jack.remove(jack[i])
            
    years += 1
            
print(jack)
population = len(jack)
print(population)
print(years)

