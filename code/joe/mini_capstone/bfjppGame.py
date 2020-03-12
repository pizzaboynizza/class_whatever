from bfjppParser import Stack, parse, pCompile
from copy import deepcopy
from draw import showMessage

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
        ret = f"[{self.p1_line}]{' '*(5 - len(str(self.p1_line)))}" #displaying p1 info
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
        ret += f"{' '*(5 - len(str(self.p2_line)))}[{self.p2_line}]" #displaying p2 info

        return ret

# find what line the program is currently on
def findLine(code, pos):
    while pos > 0:
        if code[pos][0] == "\n":
            return code[pos][1]
        pos -= 1
    return 0


#call stack = (start, loops)

#return (cmd(<>+-.?X), new i pos, line)
def oneTurn(code, pos, stk, line):
    codelen = len(code)
    while pos < codelen:
        # if test: print(f"{code[pos][0]}", end = "", flush=True)# @ {pos}\t|\t{stk.stk}")
        if code[pos][0] in "+-<>.":
            return (code[pos][0], pos + 1, line)
        elif code[pos][0] in "[]":
            return ("?", pos, line)
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
        elif code[pos][0] == "\n":
            line = code[pos][1]
        elif code[pos][0] == "EOP":
            pass
        else:
            print(f"ERROR! {code[pos]} @ ")
        
        pos += 1
    if pos >= codelen:
        pos = codelen - 1
    # print(f"ERROR! {code[pos]} @ {pos}")
    return ("X", pos, line if line!= -1 else findLine(code, pos))

# return new position or modifies the tape
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

# handles the [ and ] instructions
def turnConditional(code, pos, value, line):
    if code[pos][0] == "[":
        if value:
            return pos + 1, line
        else:
            return code[pos][1] + 1, findLine(code, pos)
    else:
        if value:
            return code[pos][1] + 1, findLine(code, pos)
        else:
            return pos + 1, line


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
        #instruction pointers
        p1 = 0
        p2 = 0
        #player's position on the tape
        p1_pos = 0
        p2_pos = len(self.tape) - 1
        #flags that indicate the player's flag is 0 (flag must be zero for two consecutive turns before loss)
        p1_flag = False
        p2_flag = False
        #'call' stack of the programs, for (a)*x and (a{b}c)%x
        p1_stack = Stack()
        p2_stack = Stack()
        #command that the player executed this turn; for recording of history
        p1_cmd = ""
        p2_cmd = ""
        #flags that indicate a loss
        p1_lose = False
        p2_lose = False
        #current line number of program; used to just use findLine() all the time, but that caused major slowdown on some programs
        p1_line = 0
        p2_line = 0
        while self.turns < 100000:
            p1_cmd, p1, p1_line = oneTurn(self.p1_code, p1, p1_stack, p1_line)
            p2_cmd, p2, p2_line = oneTurn(self.p2_code, p2, p2_stack, p2_line)

            if p1_cmd == "?":
                p1_cmd = self.p1_code[p1][0]
                p1, p1_line = turnConditional(self.p1_code, p1, self.tape[p1_pos] != 0, p1_line)
            if p2_cmd == "?":
                p2_cmd = self.p2_code[p2][0]
                p2, p2_line = turnConditional(self.p2_code, p2, self.tape[p2_pos] != 0, p2_line)

            p1_pos = turnAction(self.tape, p1_cmd, p1_pos, True, self.polarity)
            p2_pos = turnAction(self.tape, p2_cmd, p2_pos, False, False)

            self.history.append(Turn(self.tape, p1_pos, p2_pos, p1_cmd, p2_cmd, p1_line, p2_line))

            # p1_hist = p1
            # p2_hist = p2

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
        print(self.winner)

    def save(self, p1, p2, screen, font):
        showMessage("Enter filename in terminal", screen, font, (0x0, 0xFF, 0x0), 1200, 600)
        filename = input("Enter filename to save to (enter nothing to cancel): ")
        if filename == "":
            print("Save cancelled!")
        else:
            with open(filename, "w") as file:
                file.write(f"{self.title()} ({p1} vs {p2})\n\n")
                for i in range(len(self.history)):
                    file.write(f"{' '*(5-len(str(i)))}{i}:  {str(self.history[i])}\n")
            print("File Saved!")

# Testing
if __name__ == "__main__":
    import bfjppWeb as web
    import profile

    p1 = web.loadProgram("ais523_margins3")
    p2 = web.loadProgram("Gregor_furry_furry_strapon_pegging_girls")

    p1_code = pCompile(parse(p1))
    p2_code = pCompile(parse("->++>-->>+>>->+>+(>[(+)*9[-].[.+]])*2(+<)*4(+)*23<(-)*23<(-)*30<(+)*30<(-)*30<(+)*29(>)*9++(>[(+)*16[-].[.+]][-[+]])*19"))

    for pol in range(2):
        for i in range(10, 31):
            print(f"Tape length {i}{', polarity inverted' if pol==1 else ''}")
            game = Game(i, False if pol==0 else True, p1_code, p2_code)
            profile.run("game.play()")
            # game.play()
            # print(f"\t{game.winner}")
        
