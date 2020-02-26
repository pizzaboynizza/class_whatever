#problem1
def is_even(a):
    if a % 2 == 0:
        return True
    return False
# print(is_even(36))
# print(is_even(37))

#problem2
def opposite(a,b):
    if a < 0 < b or b < 0 < a:
        return True
    return False

# print(opposite(2, -100))

#problem3
def near_100(a):
    if 90 < a < 110:
        return True
    else:
        return False
# print(near_100(91))
# print(near_100(108))
# print(near_100(189))

#problem4
def maximum_of_three(a, b, c):
    if c < a > b:
        return a
    if a < b > c:
        return b
    elif a < c > b:
        return c
    else:
        pass
#print(maximum_of_three(6, 7, 7))

#problem5
def powers_of(a, b, c):
        for i in range(b, c):
             print(a ** i)

        
powers_of(2, 0, 20)







