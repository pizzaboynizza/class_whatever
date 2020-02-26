
jack = [0 , 0]
years = 0

while len(jack) <= 1000:
   
    for i in range(0, len(jack)):
        if 4 <= jack[i] <= 8:
            jack[i] += 1
            jack.append(0)
        else:
            jack[i] += 1
    print(jack)

    for i in range(0, len(jack)):
        if jack[i] == 10:
            jack.remove(jack[i])
            print(jack)
        else:
            print('nope!')
    print(jack)

    # for j in jack:
        # if jack[i] == 10:

        # jack.remove(10)

    
    # for j in jack:
    #     if jack[i] == 10:
    #         jack.remove(10)

    # for i in range(0, len(jack)):
    #     if jack[i] == 10:
    #         jack.remove(10)
    # for i in range(len(jack)):
    #     if 4 <= jack[i] <= 8:
    #         jack[i] += 1
    #         jack.append(0)
        # elif jack[i] == 10:
        #     jack.remove(10)
        # else:
        #     jack[i] += 1
        # if jack[i] >= 10:
        
        #     jack.pop(jack[i])

population = len(jack)    

            
print(population)
print(jack)

# if jack[i] == 10:
#             jack.count(10)
#             print(jack)
#             # jack.remove(10)
