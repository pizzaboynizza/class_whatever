### Take input of of 2 numbers, check each number intbetween numbers to see the value of it.


# user1 = input("Number: ")
# user2 = input("Number: ")

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


peak1 = []
valley1 = []


def peak(x):
    for num in range(1, len(x)-1):
        if x[num+1] < x[num] and x[num] > x[num-1]:
            peak1.append(num)
            
    

def valley(x):
    for num in range(1, len(x)-1):
        if x[num-1] > x[num] and x[num] < x[num+1]:
            valley1.append(num)
            

pka = []

def pv(peak1,valley1):
    pka1 = peak1 + valley1
    pka1.sort()
    pka.append(pka1)
    return 

    
    
peak(data)
valley(data)
pv(peak1,valley1)


print("this is peak", peak1)
print("this is valley", valley1)
print("this is a peak and valley", pka)





