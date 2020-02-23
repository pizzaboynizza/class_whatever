## A Simple Calculator ##

print("Let\'s do some math!")
print('I\'m secretly bad at math...')
print('Oh Well!  What sort of math are we doing?')
print('+ = Addition','- = Subtraction', 'x = Multiplication', '% = Division')
calc=input('Choice?   ')

if calc == "+":
    a1=int(input('First Number?  '))
    a2=int(input('Second Number? '))
    print(a1+a2)
elif calc == '-':
    s1=int(input('First Number?'))
    s2=int(input('Second Number?'))
    print(s1-s2)
elif calc == 'x':
    m1=int(input('First Number?'))
    m2=int(input('Second Number?'))
    print(m1*m2)
elif calc == '%':
    d1=int(input('First Number?'))
    d2=int(input('Second Number?'))
    print(d1/d2)
else:
    print('Not a valid function... yet.')