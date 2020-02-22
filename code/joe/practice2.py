# Practice 2
# Author : Joe
import string

# Problem 1
def double_letters(x):
    ret = ""
    for l in x:
        ret += l * 2
    return ret

# Problem 2
def missing_char(x):
    ret = []
    for i in range(len(x)):
        temp = ""
        for n in range(len(x)):
            if n != i:
                temp += x[n]
        ret.append(temp)
    return ret

# Problem 3
def latest_letter(x):
    latest = ""
    x = x.lower()
    for c in string.ascii_lowercase:
        if x.find(c) != -1:
            latest = c
    return latest

# Problem 4
def count_hi(x):
    hi = 0
    i = 0
    while i < len(x):
        x = x[i:len(x)]
        i = x.find("hi")
        if i == -1:
            break
        i += 1
        hi += 1
    return hi

# Problem 5
def cat_dog(s):
    s = s.replace("/", " ").replace("\\", " ").replace("cat", "/").replace("dog", "\\")
    cat, dog = 0, 0
    for c in s:
        if c == "/":
            cat += 1
        elif c == '\\':
            dog += 1
    return cat == dog

# Problem 6
def count_letter(let, s):
    num = 0
    for c in s:
        if c == let:
            num += 1
    return num

# Problem 7
def lower_case(s):
    return s.lower().strip()

# Results
print(f"double_letters('hello') -> {double_letters('hello')}")
print(f"double_letters('world') -> {double_letters('world')}\n")

print(f"missing_char('kitten') -> {missing_char('kitten')}")
print(f"missing_char('cat') -> {missing_char('cat')}\n")

print(f"latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis') -> {latest_letter('pneumonoultramicroscopicsilicovolcanoconiosis')}")
print(f"latest_letter('supercalafragalisticexpialidocious') -> {latest_letter('supercalafragalisticexpialidocious')}\n")

print(f"count_hi('hihi') -> {count_hi('hihi')}")
print(f"count_hi('hi tahini hiro ihi') -> {count_hi('hi tahini hiro ihi')}\n")

print(f"cat_dog('catdog') -> {cat_dog('catdog')}")
print(f"cat_dog('catcat') -> {cat_dog('catcat')}")
print(f"cat_dog('catdogcatdog') -> {cat_dog('catdogcatdog')}\n")

print(f"count_letter('i', 'antidisestablishmentterianism') -> {count_letter('i', 'antidisestablishmentterianism')}")
print(f"count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis') -> {count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis')}\n")

print(f"lower_case('SUPER') -> {lower_case('SUPER')}")
print(f"lower_case('        NANNANANANA BATMAN        ') -> {lower_case('        NANNANANANA BATMAN        ')}\n")