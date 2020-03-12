
import string
import random

#Define the following functions:
#peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
#valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
#peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.


#thinking out loud
#to create mountains vertically
#fist position is 'position, the second is the value of the data in that position. i.e. (position, data)
#instead of data, position

num_of_stars = [1,	2,	3,	4,	5,	6,	7,	6,	5,	4,	5,	6,	7,	8,	9,	8,	7,	6,	7,	8,	9]  #i used stars, pretty bad ass!

position = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # the indexes!
peaks = [] #empty list for peaks
troughs = [] #empty list for troughs

#Peakfinder!
def peaker(num_of_stars):
    for n in range(0,len(num_of_stars)-1):
        prev_num = num_of_stars[n-1] #this number is lower than the middle
        current_num = num_of_stars[n] #this number is higher than the others around it
        next_num = num_of_stars[n+1] #this number is lower than the middle one!
        #print(next_num) see where we're at
        #print(prev_num) see where we're at
        if prev_num < current_num > next_num:   #if it's a peak
            peaks.append(n)                     # add it to the peaks list!
    print(f'peaks are at: {peaks}')
    return(peaks)
#Trough Finder!
def trougher(num_of_stars):
    for n in range(1,len(num_of_stars)-1):
        prev_num = num_of_stars[n-1] #this number is higher than the others around it
        current_num = num_of_stars[n] #this number is lower in the middle
        next_num = num_of_stars[n+1] #this number is higher than the others around it
        #print(next_num)
        #print(prev_num)
        if prev_num > current_num < next_num:   #if it's a trough
            troughs.append(n)          #add it to troughs
    print(f'troughs are at: {troughs}')
    return(troughs)

peaker(num_of_stars)
trougher(num_of_stars)

# This function orders the indicies!
def peaker_trougher_orderer(num_of_stars):
    '''
    orders these puppies!
    '''
    p = peaker(num_of_stars)
    t = trougher(num_of_stars)
    return sorted(p + t)

ordered = peaker_trougher_orderer(num_of_stars)
print(ordered)

#Making a beautiful sideways mountain!

r = 0
q = len(position)
print(q)
while r < q-1:
    newbie = num_of_stars[r]
    print('*' * newbie)
    r += 1 
else:
    print("MOUNTAINS!!!")

#Maybe not what you hand in mind? :-)

print('                            X           X')
print('                          X X X       X X')
print('            X           X X X X X   X X X') 
print('          X X X       X X X X X X X X X X')
print('        X X X X X   X X X X X X X X X X X')
print('      X X X X X X X X X X X X X X X X X X')
print('    X X X X X X X X X X X X X X X X X X X')
print('  X X X X X X X X X X X X X X X X X X X X')
print('X X X X X X X X X X X X X X X X X X X X X')



#______Here's a bunch of notes/functions that didn't work etc. :-)
# if prev_num < n:
# if next_num < n:
# print(f"We have a peak! at {n}!")
# peaks.append(n)
# return:
# peaks
#        if next_num > n:
#            print("slopin' up!")
#    if prev_num > n:
#        print("Slopin' down!")
#        if next_num < n:
#            print("sloping down!")
#        if next_num > n:
#            print("we have a trough!")
#           troughs.append(n)

#def trougher(num_of_stars):
#peaker(num_of_stars)
#print(peaks)
#print(troughs)