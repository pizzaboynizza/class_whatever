
# """ # """ Lab 18: Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# you want to look through the data starting at index 1 and ending at index 19
# because 1 and 9 in the data cant be peaks or valleys because its nothing on both sides.
# len(data)-1) -1 must be on outside of parenthesis to avoid len([]-1). You cannot subtract one
# from a list. data[num] is how you look through the list data.
# best practice to make empty list inside the function. In order to print the function you must save
# the information in the function. Make sure it is indented inside the function and not in for loop.
# Save the return value inside a variable then print it or just print the entire function.

def peak(data):
    peak1 = []
    for num in range(1, len(data)-1):
        if data[num-1] < data[num] and data[num + 1] < data[num]:
            peak1.append(num)
    return(peak1)
print(peak(data))

#peak(data) must be used after its defined. it cannot be used above the function.
# we saved peak(data) into a variable so that we could add it to valley[data]. 
# We wanted to get a list that was a combination of both functions. so we saved both
# functions into a variables and added them together.
peak = peak(data)



def valley(data):
    valley1 = []
    for num in range(1, len(data)-1):
        if data[num-1] > data[num] and data[num + 1] > data[num]:
            valley1.append(num)
    return(valley1)
print(valley(data))

valley = valley(data)

peak_and_valley = valley + peak
print(peak_and_valley)

