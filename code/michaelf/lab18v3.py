data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
def peaks(x):
    peaks = []
    for i in range(1, len(x)-1):
        if  x[i-1] < x[i] > x[i+1]:
            if x[i] != max(x):
                peaks.append(i)
    for i in range(len(x)):
        if x[i] == max(x):
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

# print(peaks_and_valleys(data))

def between_peaks(x):
    between_peaks = []
    peak = peaks(x)
    for i in range(len(x)):
        for j in range(0, len(peak)-1):
            if  peak[j] < i < peak[j+1]:
                between_peaks.append(i)
    return between_peaks

print(between_peaks(data))

def shortest_nearby_peak(i, x):
    peak = peaks(x)
    for j in range(0, len(peak)-1):
        if peak[j] < i < peak[j+1]:
            return min(data[peak[j]], data[peak[j+1]])

def print_mountains(x):
    between = between_peaks(x)
    water = 0
    peak = peaks(x)
    for j in range(max(x), 0, -1):
        pr = ''
        for i in range(len(x)):
            if x[i] >= j :
                pr += 'X '
            elif i in between:
                if shortest_nearby_peak(i, x) >= max(x) or x[j] >= min(peak):
                    pr += '0 '
                    water += 1
                else:
                    pr += '  '  
            else:
                pr += '  '
     
        print(pr)
    print (water)

        
print_mountains(data)


