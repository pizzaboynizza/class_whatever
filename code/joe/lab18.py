# Lab 18
# Author : Joe

from random import randint

def peaks_and_valleys(data):
    ret = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            ret.append((i, "V"))
        elif data[i] > data[i-1] and data[i] > data[i+1]:
            ret.append((i, "P"))
    return ret

def valleys(data):
    ret = []
    for i in range(1, len(data)-1):
        if data[i] < data[i-1] and data[i] < data[i+1]:
            ret.append(i)
    return ret

def peaks(data):
    ret = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1]:
            ret.append(i)
    return ret

def maxList(data): #return largest number in list
    ret = data[0]
    for n in data:
        if n > ret:
            ret = n
    return ret

def draw(data):
    print("")
    for y in range(maxList(data), 0, -1): #highest point on the graph should be the greatest number in the list
        for x in range(len(data)): #width of the graph should be width of the list
            if data[x] >= y:
                print("X  ", end="")
            else:
                print("   ", end="")
        print("")
    for d in data:
        if d < 10 and d > -1:
            print(f"{d}  ", end="")
        else:
            print(f"{d} ", end="")

def drawWater(data):
    # pv = peaks_and_valleys(data)
    # (original height, water height)
    wdata = [[d, 0] for d in data]
    # for i in range(len(pv)):
    #     if pv[i][1] == "V":
    #         if i != 0:
    #             left_peak = pv[i-1][0]
    #         else:
    #             left_peak = 0 #if a valley is the first thing, then the very first data point should be the highest
    #         if i != (len(pv)-1):
    #             right_peak = pv[i+1][0]
    #         else:
    #             right_peak = len(data)-1
    #         for n in range(left_peak, right_peak+1):
    #             wdata[n][1] = min(data[left_peak], data[right_peak]) # set the water height

    for i in range(len(data)):
        if i != len(data)-1 and data[i] > data[i+1] and wdata[i][1] == 0:
            water = data[i]
            failure = True
            while failure and water > 0:
                other_side = False
                for j in range(i+1, len(data)): # check to make sure there is a retaining wall on the other side
                    if data[j] >= water:
                        other_side = True
                        break
                if other_side:
                    for j in range(i+1, len(data)):
                        if data[j] >= water:
                            failure = False
                            break
                        wdata[j][1] = water
                water -= 1

    #Draw
    print("\n")
    for y in range(maxList(data), 0, -1):
        for x in range(len(data)):
            if wdata[x][0] >= y:
                print("X  ", end="")
            elif wdata[x][1] >= y:
                print("O  ", end="")
            else:
                print("   ", end="")
        print("")
    for d in data:
        if d < 10 and d > -1:
            print(f"{d}  ", end="")
        else:
            print(f"{d} ", end="")

def displayResults(num, data):
    print(f"\n{'*'*30}Data Set {num}{'*'*30}")
    print(data)
    print("Peaks: ", peaks(data))
    print("Valleys: ", valleys(data))
    print("Peaks and valleys: ", peaks_and_valleys(data))
    draw(data)
    drawWater(data)

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data2 = [9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 5, 4, 5, 6, 7, 6, 5, 4, 3, 2, 9]
data3 = [7, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data4 = [1, 2, 3, 4, 5, 5, 5, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5]
data5 = [randint(0, 9) for i in range(len(data))]
data6 = [7, 1, 8, 4, 5, 3, 5, 6, 9, 0, 1, 6, 7, 2, 2, 6, 1, 7, 7, 6, 6]

displayResults(1, data)
# displayResults(2, data2)
# displayResults(3, data3)
# displayResults(4, data4)
displayResults(2, data5)
# displayResults(6, data6)