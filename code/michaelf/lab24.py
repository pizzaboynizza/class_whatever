import datetime
from sys import argv

def load_file(filename):
    contents = []
    with open(filename, 'r') as f:
        text = f.read()
    text = text.splitlines()
    for line in text[11:len(text)]:
        data = line[0:18]
        data = data.split()
        if data[1] != '-':
            data = data[0], int(data[1])
            data = tuple(data)
            contents.append(data)
        # data = tuple(data)
        # print(data)
        # contents.append(data)
    return contents
contents = load_file('pcc_cascade.rain.txt')
print(contents)

def mean(contents):
    count = 0
    unknown = 0
    for i in range(len(contents)):
        date, total = contents[i]
        if total != '-':
            count += total
        else:
            unknown += 1
    mean = count / (len(contents)-unknown)
    return mean, unknown
mean,unknown = mean(contents)
print(mean)
print(unknown)

def variance(contents, mean, unknown):
    squared_differences = 0
    for i in range(len(contents)):
        date, total = contents[i]
        if total != '-':
            squared_differences += (total - mean)**2
    print(squared_differences)
    variance = squared_differences/(len(contents)-unknown)-1
    return variance
print(variance(contents, mean, unknown))

def rainiest_day(contents):
    contents = contents.sort(key=lambda tup: tup[1])
    rainiest_day = contents[-1][0]
    print(contents)
    return rainiest_day
print(rainiest_day(contents))
