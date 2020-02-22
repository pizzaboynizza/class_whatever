'''
Nick Barker
Lab 20
2/20/2020
'''
cc = []
#put your empty list outside of your loop PEOPLE!

numba = (input("Please enter your 13-19 digit credit card number (nospaces)"))
#this is the input, i'll make it into an int later

#added numbers to a list
cc.append(numba)
print(cc)

#convert the input strings into a list of ints
output = list(map(int, str(cc[0])))
print(output)

#slice off the last digit. that is the check digit 
ccpop = (output.pop(-1))
print(ccpop)

#reverse the digits
outrev = (output[::-1])
print(outrev)

#double every other element in the reversed list
outrevtwice = [outrev[i] * 2 if i % 2 == 0 else outrev[i] for i in range(len(outrev))]
print(outrevtwice)

#if greater than 9, subtract 9!
niner = [i - 9 if i > 9 else i for i in outrevtwice]
print(niner)

#sum all values
yee = sum(niner)
print(f"Your grand total is {yee}")

#take the second digit of that sum if that matches the check digit, the whole card number is valid

if int(str(yee)[-1]) == ccpop:
    print("This CC is Valid!")
else:
    print("This CC is INVALID, this means certain death!")