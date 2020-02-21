print("Simple Calculator")

calc = {
'add': '+',
'subtraction': '-',
'multiplication': '*',
'division': '/',
}


operation = input("What operation: ")
num1 = input("First Number: ")
num2 = input("Second Number: ")

a = int(num1)
b = int(num2)

if calc[operation] == 'add':
    print(f"{a} + {b} =")
    print(a+b)
elif calc[operation] == 'subtraction':
    print(f"{a} - {b} =")
    print(a-b)

elif calc[operation] == 'multiplication' :
    print(f"{a} * {b} =")
    print(a*b)

elif calc[operation] == 'division':
    print(f"{a} / {b} =")
    print(a/b)


# if operation in calc:
     

# def calc(math):
#     {'add': '+',
#     'subtraction': '-',
#     'multiplication': '*',
#     'division': '/'
#     }

#     operation = input("What operation: ")
  
    


#     # if operation in olist:
#     #     return num1 operatio num2

    
    
#    def calc(num1, num2):
#        if user_input = +:
#            num1 + num2
#         elif user_input = -:
#            num1 - num2

#     olist = ('+','-','*','/',)



#   num1 = input(int("First Number: "))
#     num2 = input(int("Second Number: "))
     
 
# operation = input("What operation: ")
# num1 = ("First Number: ")
# num2 = ("Second Number: ")


# a = int(num1)
# b = int(num2) 

#     if operation == '+':   
#         a + b
#     elif operation == '-':   
#         a - b
#     elif operation == '*':   
#         a * b
#     elif operation == '/':   
#         a / b





     
    



