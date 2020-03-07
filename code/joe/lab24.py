# Lab 24
# Author : Joe

import datetime
import matplotlib.pyplot as plt

with open("data/rain.txt") as file:
    lines = file.read().split("\n")

lines.pop(0)
lines.pop(0)
lines.pop(0) # these are to get rid of non data lines of text

data = []
debug_count = 4
for t in lines:
    t = t.split()
    if t[1] == "-":
        t[1] = 0
    data.append((datetime.datetime.strptime(t[0], "%d-%b-%Y"), int(t[1])))

# Version 2

sum = 0
var_sum = 0
for d in data:
    sum += d[1]
    

mean = sum / len(data)
print(f"Mean = {mean}")

for d in data:
    var_sum += (d[1] - mean) ** 2

variance = var_sum / len(data)
print(f"Variance = {variance}")

most = -1
most_date = 0

for d in data:
    if d[1] > most:
        most_date = d[0]
        most = d[1]

print(f"Date with most rain is {most_date.strftime('%d-%b-%Y')} with {most} rainfall")

yearly_rain = dict()
yearly_points = dict()
for d in data:
    if yearly_rain.get(d[0].year, "") == "":
        yearly_rain[d[0].year] = d[1]
        yearly_points[d[0].year] = 1
    else:
        yearly_rain[d[0].year] += d[1]
        yearly_points[d[0].year] += 1

most_average = -1
most_avg_year = 0
for d in yearly_rain.keys():
    if yearly_rain[d] / yearly_points[d] > most_average:
        most_average = yearly_rain[d] / yearly_points[d]
        most_avg_year = d

print(f"The year with the most rainfall on average is {most_avg_year} with {most_average} rainfall")

# Version 3
dates = []
rainfalls = []

for d in data:
    dates.append(d[0])
    rainfalls.append(d[1])

plt.plot(dates, rainfalls)
plt.show()