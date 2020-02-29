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
    
        
        
