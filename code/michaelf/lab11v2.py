while True:

    print("Welcome to Simple Calculator!")

    operation = (input("""What is the operation you'd like to perform? (choose and enter letter)
    a. Addition
    b. Subtraction
    c. Multiplication
    d. Division
    >"""))
    operation = operation.lower()
    operation = operation.strip(".")

    if operation in ("a","b","c", "d"):

        first_number = int(input("What is the first number?\n>"))
        second_number = int(input("What is the second number?\n"))

        if operation == "a":
            print(f"{first_number} plus {second_number} equals {first_number + second_number}.")
            
        if operation == "b":
            print(f"{first_number} minus {second_number} equals {first_number - second_number}.")
            
        if operation == "c":
            print(f"{first_number} times {second_number} equals {first_number * second_number}.")
            
        if operation == "d":
            print(f"{first_number} divided by {second_number} equals {first_number / second_number}.")
            
    else:
        print("Invalid entry. Please try again!")
        continue
    
    restart = input("""Restart Calculator? (enter number)
    1. yes
    2. no
    >""")
    if restart == "1":
        continue
    elif restart == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid entry. Please try again!")
        continue