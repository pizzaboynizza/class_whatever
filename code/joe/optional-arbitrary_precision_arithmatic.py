# Lab : Arbitrary Precision Arithmetic
# Author : Joe

# get bignum from user
def getBigNum(msg):
    temp = input(msg)
    while not temp.isdigit():
        temp = input("Must enter a number: ")
    ret = []
    for c in temp:
        ret.append(int(c))
    ret.reverse()
    return ret

# addition of bignums
def addBigNum(a, b):
    i = 0
    carry = 0
    ret = []

    if len(a) > len(b):
        big = a
        little = b
    else:
        big = b
        little = a
        
    while i < len(big):
        if i >= len(little):
            ret.append(big[i] + carry)
            carry = 0
        else:
            temp = little[i] + big[i] + carry
            carry = temp // 10
            ret.append(temp % 10)
        i += 1
    return ret

# convert bignum to string
def outBigNum(a):
    ret = ""
    for c in reversed(a):
        ret += str(c)
    return "".join(ret)

# display equation, ie: a + b = c
def displayEqu(a, b, res, calc):
    most_space = max(max(len(a), len(b)), len(res))
    print(f"""
     {" " * (most_space - len(a) + 1)}{outBigNum(a)}
    {calc}{" " * (most_space - len(b) + 1)}{outBigNum(b)}
    {"-"*(most_space + 2)}
     {" " * (most_space - len(res) + 1)}{outBigNum(res)}""")

# a part of multiplying 
def singleMul(a, mul):
    ret = []
    carry = 0
    i = 0
    while i < len(a):
        temp = (a[i] * mul) + carry
        carry = temp // 10
        ret.append(temp % 10)
        i += 1
    if carry != 0:
        ret.append(carry)
    return ret

# multiply bignums
def mulBigNum(a, b):
    to_add = []
    place = 0
    for item in b:
        if item != 0:
            temp = singleMul(a, item)
            for i in range(place):
                temp.insert(0, 0)
            to_add.append(temp)
        place += 1
    ret = to_add.pop(0)
    while to_add != []:
        ret = addBigNum(ret, to_add.pop(0))
    return ret


bignum1 = getBigNum("Enter a number: ")
bignum2 = getBigNum("Enter another number: ")

displayEqu(bignum1, bignum2, addBigNum(bignum1, bignum2), "+")

displayEqu(bignum1, bignum2, mulBigNum(bignum1, bignum2), "x")