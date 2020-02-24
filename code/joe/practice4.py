# Practice 4
# Author : Joe Dean

# Problem 1
def combine(a, b):
    ret = {}
    for i in range(len(a)):
        ret[a[i]] = b[i]
    return ret

# Problem 2
def average(d):
    total = 0
    for i in d.values():
        total += i
    return total / len(d)

# Problem 3
def unify(d):
    total = {}
    num = {}
    for item in d.keys():
        if item[0] not in total:
            total[item[0]] = d[item]
            num[item[0]] = 1
        else:
            total[item[0]] += d[item]
            num[item[0]] += 1
    return {k: total[k]/num[k] for k in total.keys()}


# Results
fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
temp = combine(fruits, prices)
print(f"fruits = {fruits}\nprices = {prices}\n")
print(f"combine(fruits, prices) -> {temp}\n")

print(f"average({temp}) -> {average(temp)}\n")

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
print(f"d = {d}")

print(f"unify(d) -> {unify(d)}\n")