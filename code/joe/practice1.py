# Practice 1
# Author : Joe

# Problem 1
def is_even(x):
    return True if x % 2 == 0 else False

# Problem 2
def opposite(a, b):
    return True if a * b < 0 else False

# Problem 3
def near_100(x):
    return 90 < x < 110

# Problem 4
def maximum_of_three(a, b, c):
    return max(a, max(b, c))

# Problem 5
def pow_2(p=0, l=[]):
    l.append(2 ** p)
    if p >= 20:
        return l
    return pow_2(p+1, l)

# Results
print(f"is_even(5) -> {is_even(5)}")
print(f"is_even(6) -> {is_even(6)}\n")

print(f"opposite(10, -1) -> {opposite(10, -1)}")
print(f"opposite(2, 3) -> {opposite(2, 3)}")
print(f"opposite(-1, -1) -> {opposite(-1, -1)}\n")

print(f"near_100(50) -> {near_100(50)}")
print(f"near_100(99) -> {near_100(99)}")
print(f"near_100(105) -> {near_100(105)}\n")

print(f"maximum_of_three(5, 6, 2) -> {maximum_of_three(5, 6, 2)}")
print(f"maximum_of_three(-4, 3, 10) -> {maximum_of_three(-4, 3, 10)}\n")

print(pow_2())