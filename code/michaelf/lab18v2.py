data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(x):
    peaks = []
    for i in range(1, len(x)-1):
        if  x[i-1] < x[i] > x[i+1]:
            peaks.append(i)

    return peaks

print(peaks(data))

def valleys(x):
    valleys = []
    for i in range(1, len(x)-1):
        if  x[i-1] > x[i] < x[i+1]:
            valleys.append(i)
    return valleys

print(valleys(data))
    
def peaks_and_valleys(x):
    peaks_and_valleys = peaks(x) + valleys(x)
    peaks_and_valleys.sort()
    return peaks_and_valleys

print(peaks_and_valleys(data))

def print_mountains(x):
    for i in range(max(x), 0, -1):
        pr = ''
        for j in range(len(x)):
            if x[j] >= i :
                pr += 'X '
            elif x[j] != i:
                pr += '  '
                   
        print(pr)

print_mountains(data)

