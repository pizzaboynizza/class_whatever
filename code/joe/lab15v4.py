# Lab 15 version 4
# Author : Joe

# 0 : invalid
# 1 : hhmm
# 2 : hmm
# 3 : hhmmAP
# 4 : hmmAP
def checkTime(t):
    if len(t) == 4 and t[0:2].isdigit() and t[2:4].isdigit():
        return 1
    elif len(t) == 3 and t[0:1].isdigit() and t[1:3].isdigit():
        return 2
    elif len(t) == 6 and t[0:2].isdigit() and t[2:4].isdigit() and t[4] in "ap" and t[5] == "m":
        if t[0:2] == "00":
            return 0
        return 3
    elif len(t) == 5 and t[0:1].isdigit() and t[1:3].isdigit() and t[3] in "ap" and t[4] == "m":
        if t[0:1] == "0":
            return 0
        return 4
    else:
        return 0

def getHours(t, kind):
    if kind == 1 or kind == 3:
        ret = int(t[0:2])
    elif kind == 2 or kind == 4:
        ret = int(t[0:1])
    else:
        return -1
    if kind == 3 or kind == 4:
        ap = 1 if (kind == 3 and t[4] == "p") or (kind == 4 and t[3] == "p") else 0
        if ap == 0 and ret == 12:
            ret = 0
        elif ap == 0 and ret > 12:
            ret = 24 # can't have 13:00 a.m!
        elif ap == 1 and ret != 12:
            ret += 12
    return ret

def getMin(t, kind):
    if kind == 1 or kind == 3:
        return int(t[2:4])
    elif kind == 2 or kind == 4:
        return int(t[1:3])
    else:
        return -1

def ensureTime(msg):
    en = input(msg).replace(" ", "").replace(":", "").replace(".", "").lower()
    check = checkTime(en)
    if check == 0 or getHours(en, check) > 23 or getMin(en, check) > 59:
        return ensureTime("Must enter a valid time: ")
    return en

single_digit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
double_digit = ["", "UNUSED", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]
teens_case = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def spellNum(x, zero, one):
    ones_place = x % 10
    tens_place = x // 10

    if x == 0:
        return zero
    elif 10 <= x < 20:
        return teens_case[ones_place]
    elif x < 10:
        return one + single_digit[ones_place]
    else:
        return double_digit[tens_place] + (" " if tens_place != 0 and ones_place != 0 else "") + single_digit[ones_place]


raw = ensureTime("Enter time: ")

hours = getHours(raw, checkTime(raw))
minutes = getMin(raw, checkTime(raw))

# 12 hour time:
time12_h = hours % 12 if hours % 12 != 0 else 12
time12_ap = "a.m." if hours < 12 else "p.m."
time12 = spellNum(time12_h, "ERR", "") + " " + spellNum(minutes, "o'clock", "oh ") + " " + time12_ap

print("12 Hour Format:\t", time12)

# 24 hour time:
time24 = spellNum(hours, "zero", "oh ") + " " + spellNum(minutes, "hundred", "oh ")

print("24 Hour Format:\t", time24)