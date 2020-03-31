'''Lab 18: Peaks and Valleys
Define the following functions:

peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.'''

mountain_level= [1,2,3,4,5,6,7,6,5,4,5,5,7,8,9,8,7,6,7,8,9]

# i = len(mountain_level)
#create function for peak
# peak has lower number on left and right
# function needs take in data

def peak_num(mountain_level):
    peaks =[]
    
# for each number in mountian_level, do something:
    for i in range (1,len(mountain_level)-1): #checks number from 1-lastnumber
#check to see if numbers to the left and right are lower than numbers[i]
#ASK HOW -1 AND +1 WORK
        if mountain_level[i] > mountain_level[i-1] and  mountain_level[i] > mountain_level[i+1]:   #compares number[i] with Land R #
            peaks.append(i) #append numbers[i] to empty peak list
    return peaks  
print(peak_num(mountain_level))

# create functions for valleys
#valley is a numner with  higher numner on left and right

def valley_nums(mountain_level):
    valleys = []
    for i in range (1,len(mountain_level)-1):
        if mountain_level[i-1] > mountain_level[i] < mountain_level[i+1]:
            valleys.append(i)
    return valleys
print(valley_nums(mountain_level))

# peaks_data = peak_num(mountain_level)
# valleys_data = valley_nums(mountain_level)
# print(peaks_data + valleys_data)
peaks_and_valleys =[]
peaks_and_valleys.append(peak_num(mountain_level) + valley_nums(mountain_level))
print(peaks_and_valleys)

#OR

print(f" peaks_and_valleys is {peak_num(mountain_level) + valley_nums(mountain_level)}")


# peaks_valleys = peaks + valleys
# print(peaks_valleys)
# peaks.extend(valleys)
# peak_valleys.append
# print(peaks_valleys)
# def peaks_n_valleys(mountain_level):
#     for peaks, valleys in mountain_level.items():
#         peaks.extend(valleys)

#         return peak_valleys
# print(peaks_n_valleys(mountain_level))


