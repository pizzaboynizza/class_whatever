data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9,]

def peaks_and_valleys(data):

    for i in range(1, len(data)-1):
        if data[i - 1] < data[i] > data[i + 1]:
            print(i)

        elif data[i - 1] > data[i] < data[i + 1]:
            print(i)

peaks_and_valleys(data)
#


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# def graph_peaks_and_valleys(data):
# #
#     for y in range(max(data), 0, -1):
#         for x in range(len(data)):
#             if data[x] >= y:
#                 print("X ", end="")
#             else:
#                 print("", end="")
#             print("")
#             for d in data:
#                 if d < 10 and d > -1:
#                     print(f"{d}  ", end="")
#                 else:
#                     print(f"{d} ", end="")


# graph_peaks_and_valleys(data)


