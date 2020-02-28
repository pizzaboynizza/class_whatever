data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# def peaks(x):
#     #peaks defined by number in list which has 2 numbers on each side that contain LESSER values
#     # ex:     4, 5, 6, 5, 4 -> peak is 6;     for n: where x < n > y
#     peak = []
#     for num in range(1, len(x)-1):
#         if x[num-1] < x[num] and x[num] > x[num+1]:
#             # print(x[num])
#             # peak.append(x[num])
#             peak.append(num)
#     print(peak)
#     return peak

# peaks(data)

# def valleys(data):
#     #valleys defined by number in list with 2 numbers on each side that contain GREATER values
#     # ex:    6, 5, 4, 5, 6 -> valley is 4; for n: where x > n < y
#     valley = []
#     for num in range(1, len(x)-1):
#         if x[num-1] > x[num] and x[num] < x[num+1]:
#             # print(x[num])
#             # print(num)
#             # valley.append(x[num])
#             valley.append(num)
#     print(valley)
#     return valley

# peaks()
# valleys(data)

def peaks_and_valleys(x):
    # peak1 = list(x)
    # valley1 = list(y)
    # zip1 = zip(peak1, valley1)
    # sorts = sorted(zip(peak1, valley1))
    # print(zip1)
    valley = []
    peak = []
    combined = []

    def valleys(x):
        for num in range(1, len(x)-1):
            if x[num-1] > x[num] and x[num] < x[num+1]:
                valley.append(num)
                combined.append(num)
        # print(valley)
        return valley

    def peaks(x):
        for num in range(1, len(x)-1):
            if x[num-1] < x[num] and x[num] > x[num+1]:
                peak.append(num)
                combined.append(num)
        # print(peak)
        return peak

    valleys(data)
    peaks(data)
    sorted1 = sorted(combined)
    # print(combined)
    print(sorted1)
    

peaks_and_valleys(data)

# graphing values the hard way
nums = enumerate(data)
maxY = max(data)
n1 = maxY #this should start as the maximum Y-value, and represents the row we are iterating on.
n2 = len(data) #in a graph, this represents range of index values from x=0 through x=(max index of list)
# x = pass #index of list item (index of Y-value for graph)
# y = pass #Value of each x index (represents verticality of the number of each X-place)

# get max(y) #original max-Y set equal to n1 for later iteration
# # for x in range(len(x)):
# while n1 > 0:
#     # for n1 > nums[y] for x in range(n2):
#     for x in range(n2):
#         if n1 > nums(y):
#             print(" ")
#             n1 -= 1
#         elif nums(y) <= n1:
#             print("X")
#             n1 -= 1
    # for nums[y] <= n1 for x in range(n2):
        # print("X")
        # n1 -= 1
graphRow = []
for y in range(n1, 0, -1):
    for x in range(len(data)):
        if data[x] < y:
            print(" ", end="")
            # graphRow.append(" ")
            # print("".join(graphRow))
        elif data[x] >= y:
            print("X", end="")
            # graphRow.append("X")
            # print("".join(graphRow))
    # str(graphRow)
    # print("".join(graphRow))
    # print(graphRow)

    print()