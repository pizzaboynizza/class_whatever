'''
Define the following functions:

1. peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

2. valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

3. peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.
'''


data = []
while True:
  user_input = input("To determine peaks and valleys in your data, enter one number at a time (in the order of your data) and then press a blank enter when complete: ")
  if user_input:
    data.append(float(user_input))
  else:
    break
print(data)

# def peaks():
peaks = []
for i in range(1, len(data)-1):
    left = data[i-1]
    middle = data[i]
    right = data[i+1]
    if left < middle > right:
        peaks.append(i)
        # print(f"The data number/s at index/es {peaks} is a/are peak(s) (index begins at 0)")
print(f"The peaks are at the following indexes: {peaks}")
    # return peaks
    

valleys = []
for i in range(1, len(data)-1):
    left = data[i-1]
    middle = data[i]
    right = data[i+1]
    if left > middle < right:
        valleys.append(i)
        # print(f"The data number/s at index/es {peaks} is a/are peak(s) (index begins at 0)")
print(f"The valleys are at the following indexes: {valleys}")


peaks_and_valleys = peaks + valleys
print(f"The peaks and valleys are at the following indexes: {sorted(peaks_and_valleys)}")