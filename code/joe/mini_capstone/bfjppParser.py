import re


#take string and turn into list of valid commands
def parse(prgm):
    parsed = []
    i = 0
    strlen = len(prgm)
    bfj = re.compile(r"\+|-|>|<|\.|\n|\[|\]|\(|\{|\}|(\)(\*|%)-?\d+)")
    while i < strlen:
        temp = bfj.search(prgm[i:])
        if temp != None:
            parsed.append(temp.group())
            i += temp.end()
        else:
            #print(f"Unknown error while parsing file at position {i}/{strlen}") #got an error for temp being None, unsure of cause
            i = strlen # pretty sure the cause is comments at the end of a program, so let's just end the parsing
    return parsed

class Stack:
    def __init__(self):
        self.stk = []

    def push(self, p):
        self.stk.append(p)

    def pop(self):
        return self.stk.pop(-1)

    def top(self):
        return self.stk[-1]

    def isEmpty(self):
        if self.stk == []:
            return True
        return False


# '[', end / ']', start / '(', end, times, curly_end / ')', start / '{', end, paren_start
# is curly_end necessary?
def pCompile(prgm):
    line = 0
    paren = Stack()
    bracket = Stack()
    curly = Stack()
    ret = []
    prgmsize = len(prgm)
    i = 0
    while i < prgmsize:
        if prgm[i] in "+-><.":
            ret.append([prgm[i]])
        elif prgm[i] == "[":
            ret.append(["[", -1])
            bracket.push(i)
        elif prgm[i] == "(":
            ret.append(["(", -1, 0, -1])
            paren.push(i)
        elif prgm[i] == "{":
            if paren.isEmpty():
                print("ERROR! No '(' to match with '{' on line", line)
                ret.append(["{", -1])
            else:
                ret.append(["{", paren.top()])
                curly.push(i)
        elif prgm[i] == "\n":
            line += 1
            ret.append(["\n", line])
        elif prgm[i] == "]":
            if bracket.isEmpty():
                print(f"ERROR! Unmatched ']' on line {line}")
                ret.append(["]", -1])
            else:
                ret.append(["]", bracket.top()])
                ret[bracket.pop()][1] = i #set the end position of the matching starting bracket to this
        elif prgm[i] == "}":
            if curly.isEmpty():
                print("ERROR! Unmatched '}' on line", line)
                ret.append(["}", -1])
            else:
                ret.append(["}", curly.top()])
                if paren.isEmpty():
                    print("ERROR! No '(' to match with '}' on line", line)
                else:
                    ret[paren.top()][3] = i
                ret[curly.pop()][1] = i
        elif prgm[i][0] == ")":
            if paren.isEmpty():
                print(f"ERROR! Unmatched ')' on line {line}")
                ret.append([")", -1])
            else:
                try:
                    temp = int(prgm[i][2:])
                except:
                    print(f"ERROR! Invalid number {prgm[i]} on line {line}")
                    temp = 0
                ret.append([")", paren.top()])
                ret[paren.top()][1] = i
                ret[paren.pop()][2] = temp
        else:
            print(f"ERROR! Unknown command {prgm[i]} on line {line}")
            
        i += 1
    ret.append(["EOP"]) # end of program; I've forgotton why I've included this in here, but I'm sure it's important

    # Unmatched (, [, and {; set there endpoints to themselves, which should mean the interpreter will just skip them
    for p in paren.stk:
        print(f"ERROR! Unmatched ( on {p}")
        ret[p][1] = p
    for p in bracket.stk:
        ret[p][1] = len(ret) - 1 # except for [, which sets its end point to the end of the program
        print(f"ERROR! Unmatched [ on {p}")
    for p in curly.stk:
        ret[p][1] = p
        print("ERROR! Unmatched { on", p)
    return ret

# Testing
def printList(l):
    i = 0
    for e in l:
        print(i, e)
        i += 1


if __name__ == "__main__":
    import bfjppWeb as web

    p = web.loadProgram("quintopia_space_elevator")

    pCompile(parse(p))