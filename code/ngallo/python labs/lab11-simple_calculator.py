while True:

    operation = input("What is the operation (+, -, * or /) you'd like to perform? ")
    first_number = int(input("What is the first number? "))
    second_number = int(input("What is the second number "))


    if operation == "+":
        addition = (first_number + second_number)
        print(addition)

    elif operation == "-":
        subtration = (first_number - second_number)
        print(subtration)

    elif operation == "*":
        multiply = (first_number * second_number)
        print(multiply)

    elif operation == "/":
        divid = (first_number / second_number)
        print(divid)

    else:
        print("Error, try again!")