while True:

    print("Welcome to Simple Calculator!")

    operation = input("Plug in your equation!:")
    
    operation = operation.strip("=")
    
    print(f"{operation} equals {eval(operation)}.")

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