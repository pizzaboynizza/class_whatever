## Readability Score ##

import string

with open('84-0.txt','r',encoding='utf-8') as file:
    content=file.read().lower()

def chact(x:str)->int:
    ct=0
    letz=set(string.ascii_letters.lower())
    for char in x:
        if char in letz:
            ct += 1
    return ct

def line(x:str)-> int:
    ln=x.replace('?','.')
    ln=ln.replace('!','.')
    ln=ln.strip('.')
    ln=ln.split('.')
    ln=len(ln)
    return ln

def wc(x:str)->int:
    return len(x.strip().split())

scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

def mrkup(x:str)->int:
    cnum=chact(x)
    wnum=wc(x)
    snum=line(x)
    ari=int((4.71*(cnum/wnum))+(0.5*(wnum/snum))-21.43)
    if ari>14:
        ari=14
    return ari
i=mrkup(content)

print("Analyzing")
print('The ARI is', mrkup(content))
print((f'This corresponds to a {scale[i] ["grade_level"]} level of difficulty. \nThat is suitable for an average person {scale[i]["ages"]} years old.'))