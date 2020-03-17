print("Simple Calculator")

calc = {
'+': '+',
'-': '-',
'*': '*',
'/': '/',
}


operation = input("What operation: ")
num1 = input("First Number: ")
num2 = input("Second Number: ")

a = int(num1)
b = int(num2)

if calc[operation] == '+':
    print(f"{a} + {b} =")
    print(a+b)
elif calc[operation] == '-':
    print(f"{a} - {b} =")
    print(a-b)
elif calc[operation] == '*' :
    print(f"{a} * {b} =")
    print(a*b)

elif calc[operation] == '/':
    print(f"{a} / {b} =")
    print(a/b)






     
    



