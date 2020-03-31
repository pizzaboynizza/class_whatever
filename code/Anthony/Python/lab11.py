'''Lab 11: Simple Calculator
# Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17'''
while True:
    user_input= input(" Continue or done?: ")
    if user_input == "done":
        print("goodbye")
        break


    operation= input("Enter the operation you want to do: ")
    operand1 =  int(input(" Enter the number: "))
    operand2 = int(input("Enter sencond number: "))

    if operation == "+":
        print( operand1 + operand2)
    elif operation == '*':
        print (operand1 * operand2)

    elif operation == "-":
        print(operand1 - operand2)
    elif operation == "/":
        print(operand1/operand2)

  


