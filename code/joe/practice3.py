# Practice 3
# Author : Joe
import random

# Problem 1
def random_element(a):
    i = random.randint(0, len(a)-1)
    return a[i]

# Problem 2
def getList():
    ret = []
    while True:
        uin = input("Enter a number (or 'done'): ")
        if uin == "done":
            break
        if uin.isdigit():
            ret.append(int(uin))
    return ret

# Problem 3
def eveneven(a):
    even = 0
    for x in a:
        if x % 2 == 0:
            even += 1
    return True if even % 2 == 0 else False

# Problem 4
def every_other_num(a):
    i = 0
    x = []
    while i < len(a):
        x.append(a[i])
        i += 2
    return x

def every_other_num_for(a):
    x = []
    for i in range(0, len(a), 2):
        x.append(a[i])
    return x

# Problem 5
def reverse(a):
    x = []
    for i in range(-1, -len(a)-1, -1):
        x.append(a[i])
    return x

# Problem 6
def extract_less_than_ten(a):
    ret = []
    for n in a:
        if n < 10:
            ret.append(n)
    return ret

# Problem 7
def common_elements(a, b):
    ret = []
    while a != []:
        el_a = a[0]
        for el_b in b:
            if el_a == el_b:
                ret.append(el_a)
                break
        while el_a in a:
            a.remove(el_a)
    return ret

# Problem 8
def combine(a, b):
    ret = []
    for i in range(len(a)):
        ret.append(a[i])
        ret.append(b[i])
    return ret

# Problem 9
def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return [None, None]

# Problem 10
def merge(a, b):
    ret = []
    for i in range(len(a)):
        ret.append([a[i], b[i]])
    return ret

# Problem 11
def combine_all(a):
    ret = []
    for x in a:
        for y in x:
            ret.append(y)
    return ret

# Problem 12
def fibonacci(n):
    x = 1
    y = 1
    ret = []
    for i in range(n):
        if i == 0 or i == 1:
            ret.append(1)
        else:
            ret.append(x + y)
        y = x
        x = ret[i]
    return ret

# Problem 13
def minimum(numb):
    m = numb[0]
    for n in numb:
        if n < m:
            m = n
    return m

def maximum(numb):
    m = numb[0]
    for n in numb:
        if n > m:
            m = n
    return m

def mean(numb):
    m = 0
    for n in numb:
        m += n
    return m / len(numb)

# Problem 14
def find_unique(a):
    ret = []
    for x in a:
        if x not in ret:
            ret.append(x)
    return ret

# Results
fruits = ["apples", "bananas", "pears"]
print(f"fruits = {fruits}")
for loop in range(6):
    print(f"random_element(fruits) -> {random_element(fruits)}")
print()

print(f"getList() -> {getList()}\n")

print(f"eveneven([5, 6, 2]) -> {eveneven([5, 6, 2])}")
print(f"eveneven([5, 5, 2]) -> {eveneven([5, 5, 2])}\n")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(f"nums = {nums}")
print(f"every_other_num(nums) -> {every_other_num(nums)}")
print(f"every_other_num_for(nums) -> {every_other_num_for(nums)}\n")

print(f"reverse(nums) -> {reverse(nums)}\n")

print(f"extract_less_than_ten(nums) -> {extract_less_than_ten(nums)}")
print(f"extract_less_than_ten([1, 11, 111, 2, 8]) -> {extract_less_than_ten([1, 11, 111, 2, 8])}\n")

print(f"common_elements(nums, [1, 2, 4, 8, 16]) -> {common_elements(nums, [1, 2, 4, 8, 16])}\n")

print(f"combine(['a','b','c'],[1,2,3]) -> {combine(['a','b','c'],[1,2,3])}\n")

print(f"find_pair([5, 6, 2, 3], 7) -> {find_pair([5, 6, 2, 3], 7)}\n")

print(f"merge([5,2,1], [6,8,2]) -> {merge([5,2,1], [6,8,2])}\n")

print(f"combine_all([[5,2,3],[4,5,1],[7,6,3]]) -> {combine_all([[5,2,3],[4,5,1],[7,6,3]])}\n")

print(f"fibonacci(8) -> {fibonacci(8)}\n")

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(f"minimum(nums) -> {minimum(nums)}")
print(f"maximum(nums) -> {maximum(nums)}")
print(f"mean(nums) -> {mean(nums)}\n")

print(f"find_unique([12, 24, 35, 24, 88, 120, 155, 88, 120, 155]) -> {find_unique([12, 24, 35, 24, 88, 120, 155, 88, 120, 155])}\n")