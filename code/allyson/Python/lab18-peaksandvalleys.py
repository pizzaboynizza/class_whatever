## Peaks and Valleys ##

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
i = 1
peaks = []
valleys = []
peaksandvalleys = []

print("Peaks")
for i in range(len(data) - 1):
    if data[i - 1] == data[i + 1]:
        if data[i] < data[i - 1]:
            peaks.append(i)
            peaksandvalleys.append(i)

print("Valleys")
for i in range(len(data) - 1):
    if data[i - 1] == data[i + 1]:
        if data[i] < data[i - 1]:
            valleys.append(i)
            peaksandvalleys.append(i)

peaksandvalleys.sort()
print(peaks)
print(valleys)
print(peaksandvalleys)

print("Printed Chart")
row = [""] * 21
high = max(data)

while high > 0:
    for i in range(len(data)):
        if data[i] >= high:
            row[i] = "X"
        else:
            row[i] = " "
    high = high - 1
    print("".join(row))
