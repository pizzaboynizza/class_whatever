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
#print(data)
def peaks():
  # for i in range(0,len(nums_reversed),2):
  #   nums_reversed[i] *= 2
  # print(nums_reversed)
  for i in range(len(data)):
    # return i of peaks()
    if i to left and i to right < i:
    i == peak
print(peaks(i))