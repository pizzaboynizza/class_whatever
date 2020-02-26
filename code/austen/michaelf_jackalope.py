jack = [0, 0]
years = 0
population = len(jack)

# check = list(range(len(jack)-1))
# print(check)
while len(jack) <= 1000: 
    #there should be a counter here starting at 0

    #below can be simplified without the -1 ect...
    for i in range(len(jack)-1, -1, -1):
        #outside the if but within the for should live jack +

        #within this if revert back to the docs 4-8 reproductive
        if 0 <= jack[i] < 4:
            jack[i] += 1
            #insert counter +1 here 
            # if jack == 10:
            #     jack.remove(jack[i])
        

    # this elif should be a while and include count and remove 
        elif 4 <= jack[i] <= 8:
            jack[i] += 1
            jack.append(0)
            # if jack == 10:
            #     jack.remove(jack[i])
            
    #insert another for loop that appends on the new jacks, no need for the else
        else:
            pass
            # jack.remove(jack[i])
            
    years += 1
            
print(jack)
population = len(jack)
print(population)
print(years)

