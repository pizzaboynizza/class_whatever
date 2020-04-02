'''Practice 1: Fundamentals
For each practice problem, write a function that returns a value (not just prints it). You can then call the function a couple times to test it, comment those calls out, and move on to the next problem. An example of this format is given below.

#Problem 1
Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

def is_even(a):
    ...
is_even(5) → False
is_even(6) → True'''



#THIS WILL ONLY DO THE MATH AND GIVE THE ANSWER
# def int_odd(a):
#     return a%2
# print(int_odd(6))

#THIS WILL DO THE MATH AND CONTDITIONS WHEN THE MATH IS DONE
# def int_even(a):
#     if a % 2:
#         return ("odd")
#     else:
#         return ("even")
   
# print(int_even(6))

'''Write a function that takes two ints, a and b, and returns True if one is positive and the other is negative.

def opposite(a, b):
    ...
opposite(10, -1) → True
opposite(2, 3) → False
opposite(-1, -1) → False'''

def number(a,b):
    if a - b == "+" or "-":
        return ("True")
    elif a & b == "-" and "-":
        return ("False")
print(number(-1, -2))

