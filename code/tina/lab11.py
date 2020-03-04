
while True:
    op = input ("""
    Pick a math operation input the sign: 
    Addition: +
    Subtraction: -
    multiplication: *
    Division: 
    : """)
    if op not in['+','-','*','/']:
        break



    num1 = input("First Number: ")
    num2 = input("Second Number: ")

    a = int(num1)
    b = int(num2)

    if op == '+' :
        print(f"{a} + {b} = ")
        print(a+b)
    elif op == '-':
        print(f"{a} - {b} =")
        print(a-b)
    elif op == '*':
        print(f"{a} * {b} =")
        print(a*b)
    elif op == '/':
        print(f"{a} / {b} =")
        print(a/b)
    
    user1 = input("Again? ")
    if user1 not in ['yes','y','YES']:
        break

