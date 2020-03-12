from bfjppParser import Stack, parse, pCompile
from copy import deepcopy

class Turn:
    def __init__(self, tape, p1_pos, p2_pos, p1_code, p2_code, p1_line, p2_line):
        self.tape = deepcopy(tape)
        self.p1_pos = p1_pos
        self.p2_pos = p2_pos
        self.p1_code = p1_code
        self.p2_code = p2_code
        self.p1_line = p1_line
        self.p2_line = p2_line


    def __str__(self):
        ret = f"[{self.p1_line}]{' '*(4 - len(str(self.p1_line)))}" #displaying p1 info
        ret += f" '{self.p1_code}'  "

        if self.p1_pos == -1: #out of bounds on the left
            if self.p2_pos == -1:
                ret += "XAN "
            else:
                ret += ">AN "
        elif self.p2_pos == -1:
            ret += "<AN "

        for i in range(len(self.tape)): # the tape
            if self.p1_pos == i:
                if self.p2_pos == i:
                    ret += "X"
                else:
                    ret += ">"
            elif self.p2_pos == i:
                ret += "<"
            else:
                ret += " "
            ret += hex(self.tape[i]).upper()[2:]if len(hex(self.tape[i])) == 4 else '0'+hex(self.tape[i]).upper()[2:]
            ret += " "

        if self.p1_pos == len(self.tape): #out of bounds on the right
            if self.p2_pos == len(self.tape):
                ret += "XAN "
            else:
                ret += ">AN "
        elif self.p2_pos == len(self.tape):
            ret += "<AN "
        
        ret += f"  '{self.p2_code}' "
        ret += f"{' '*(4 - len(str(self.p2_line)))}[{self.p2_line}]" #displaying p2 info

        return ret
        

    def print(self):
        for t in self.tape:
            print(t, end=" ")
        print(f"\n\tP1 '{self.p1_code}' @ {self.p1_pos}\n\tP2 '{self.p2_code}' @ {self.p2_pos}")

def findLine(code, pos):
    while pos > 0:
        if code[pos][0] == "\n":
            return code[pos][1]
        pos -= 1
    return 0



#call stack = (start, loops)

#return (cmd(<>+-.?X), new i pos)
def oneTurn(code, pos, stk):
    codelen = len(code)
    while pos < codelen:
        # if test: print(f"{code[pos][0]}", end = "", flush=True)# @ {pos}\t|\t{stk.stk}")
        if code[pos][0] in "+-<>.":
            return (code[pos][0], pos + 1)
        elif code[pos][0] in "[]":
            return ("?", pos)
        elif code[pos][0] == "(":
            if code[pos][2] != 0: #make sure the repeat != 0, otherwise we'll skip
                stk.push([pos, code[pos][2]])
            else:
                pos = code[pos][1]
        elif code[pos][0] == "{":
            if stk.top()[1] == 0: #end of the loop means we start executing the middle
                pass
            elif stk.top()[1] > 0:
                stk.top()[1] -= 1
                if stk.top()[1] > 0: # stk.top() > 1: do, else don't, but stk.top() needs to be 0 when we do do
                    pos = stk.top()[0]
            else: # for -1 loops that just repeat forever
                pos = stk.top()[0]
            # print(code[pos], stk.stk)
        elif code[pos][0] == ")":
            # print(code[pos])
            if code[code[pos][1]][3] == -1:
                if stk.top()[1] > 1: # >1 because >0 would cause an extra loop
                    pos = stk.top()[0]
                    stk.top()[1] -= 1
                elif stk.top()[1] < 0:
                    pos = stk.top()[0]
                else:
                    stk.pop()
            else:
                if stk.top()[1] < 0:
                    pos = code[code[pos][1]][3]
                elif stk.top()[1] < code[code[pos][1]][2]:
                    pos = code[code[pos][1]][3]
                    stk.top()[1] += 1
                else:
                    stk.pop()
                # print(code[pos], stk.stk)
        elif code[pos][0] == "}":
            stk.top()[1] += 1
        elif code[pos][0] == "\n" or code[pos][0] == "EOP":
            pass
        else:
            print(f"ERROR! {code[pos]} @ ")
        
        pos += 1
    if pos >= codelen:
        pos = codelen - 1
    print(f"ERROR! {code[pos]} @ {pos}")
    return ("X", pos)

# return new position
def turnAction(tape, cmd, pos, left, pol):
    if (cmd == "+" and pol == False) or (cmd == "-"  and pol == True):
        tape[pos] = (tape[pos] + 1) % 256
    elif (cmd == "-" and pol == False) or (cmd == "+" and pol == True):
        tape[pos] = (tape[pos] - 1) % 256
    elif (cmd == ">" and left == True) or (cmd == "<" and left == False):
        pos += 1
    elif (cmd == "<" and left == True) or (cmd == ">" and left == False):
        pos -= 1
    return pos


def turnConditional(code, pos, value):
    if code[pos][0] == "[":
        if value:
            return pos + 1
        else:
            return code[pos][1] + 1
    else:
        if value:
            return code[pos][1] + 1
        else:
            return pos + 1


class Game:
    def __init__(self, length, polarity, p1, p2):
        self.tape = []
        for i in range(length):
            if i == 0 or i == length-1:
                self.tape.append(128)
            else:
                self.tape.append(0)
        self.polarity = polarity
        self.p1_code = p1
        self.p2_code = p2
        self.history = []
        self.turns = 0
        self.winner = "Tie Game"
    
    def numTurns(self):
        return len(self.history)

    def play(self):
        p1 = 0
        p2 = 0
        p1_hist = p1
        p2_hist = p2
        p1_pos = 0
        p2_pos = len(self.tape) - 1
        p1_flag = False #flag can be 0 for one turn before it counts as a loss
        p2_flag = False
        p1_stack = Stack()
        p2_stack = Stack()
        p1_cmd = ""
        p2_cmd = ""
        p1_lose = False
        p2_lose = False
        while self.turns < 100000:
            p1_cmd, p1 = oneTurn(self.p1_code, p1, p1_stack)
            p2_cmd, p2 = oneTurn(self.p2_code, p2, p2_stack)

            if p1_cmd == "?":
                p1_cmd = self.p1_code[p1][0]
                p1 = turnConditional(self.p1_code, p1, self.tape[p1_pos] != 0)
            if p2_cmd == "?":
                p2_cmd = self.p2_code[p2][0]
                p2 = turnConditional(self.p2_code, p2, self.tape[p2_pos] != 0)

            p1_pos = turnAction(self.tape, p1_cmd, p1_pos, True, self.polarity)
            p2_pos = turnAction(self.tape, p2_cmd, p2_pos, False, False)

            self.history.append(Turn(self.tape, p1_pos, p2_pos, p1_cmd, p2_cmd, findLine(self.p1_code, p1_hist), findLine(self.p2_code, p2_hist)))

            p1_hist = p1
            p2_hist = p2

            # check if lose
            if p1_pos < 0 or p1_pos > len(self.tape) - 1 or (self.tape[0] == 0 and p1_flag):
                p1_lose = True
            if p2_pos < 0 or p2_pos > len(self.tape) - 1 or (self.tape[-1] == 0 and p2_flag):
                p2_lose = True

            if p1_lose: #check if game over
                if p2_lose:
                    return
                self.winner = "P2 Wins"
                return
            elif p2_lose:
                self.winner = "P1 Wins"
                return

            if self.tape[0] == 0: #flags at zero
                p1_flag = True
            else:
                p1_flag = False
            
            if self.tape[-1] == 0:
                p2_flag = True
            else:
                p2_flag = False

            self.turns += 1

    def title(self):
        return f"Tape length {len(self.tape)}{', polarity inverted' if self.polarity else ''}"
    
    def print(self):
        turn = 0
        for t in self.history:
            print(f"Turn {turn}:\t", end="")
            print(t)
            turn += 1
            # if turn == 200:
            #     input()
        print(self.winner)

    def save(self, p1, p2):
        with open(input("Enter filename to save to: "), "w") as file:
            file.write(f"{self.title()} ({p1} vs {p2})\n\n")
            for i in range(len(self.history)):
                file.write(f"{' '*(5-len(str(i)))}{i}:  {str(self.history[i])}\n")
        print("File Saved!")


# p1 = ">\n(+)*64\n>(-)*64\n(>+>-)*3\n(>[-])*21"
# p2 = "(++-)*-1"


# p1_code = pCompile(parse(p1))
# p2_code = pCompile(parse(p2))

# game = Game(30, False, p1_code, p2_code)

# game.play()

# game.print()