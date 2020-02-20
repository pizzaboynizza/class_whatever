#Lab 11

valid_ops = ["+", "-", "*", "/", "//", "%", "**", "done", "eval", "help"]

def inputFloat(msg):
    try:
        result = float(input(msg))
        return result
    except ValueError:
        return inputFloat("Please enter a number: ")


while True:
    op = input("What is the operation you'd like to perform? ")
    while op not in valid_ops:
        op = input("Invalid operation, please try again (type 'help' for help): ")

    if op == "done":
        break
    elif op == "eval":
        equation = input("Please enter an arithmetic expression: ")
        result = eval(equation)
        print(f"\n{equation} = {result}\n")
    elif op == "help":
        print("Valid operations are: ")
        for x in valid_ops:
            print(f"\t{x}")
    else: #normal calculations
        num1 = inputFloat("What is the first number? ")
        num2 = inputFloat("What is the second number? ")

        if op == "/" or op == "//" or op == "%": #prevent divide by zero errors
            while num2 == 0.0:
                num2 = inputFloat("Can't divide by zero, enter another number: ")

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "//":
            result = num1 // num2
        elif op == "%":
            result = num1 % num2
        elif op == "**":
            result = num1 ** num2
        else:
            result = "ERROR" #shouldn't be able to get here

        print(f"\n{num1} {op} {num2} = {result}\n")

print("Goodbye!")