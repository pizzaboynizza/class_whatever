#problem1
def double_letters(x):
    double_x = [char * 2 for char in x]
    print(''.join(double_x))

x = input("give me a word: ")
# double_letters(x)

#problem2
import random
def missing_char(x):
    
    new_list = []
    [new_list.append(x.replace(x[i], '', 1)) for i in range(0, len(x))]
    # [it.slice(i) for i in range(0, len(new_list))]
    print(new_list)


x = input("give me a word: ")
missing_char(x)