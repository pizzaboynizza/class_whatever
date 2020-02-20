

while True:

    user_operation = input("What is the operation you'd like to perform?")

    user_first_number = float(input("What is the first number?"))

    user_second_number = float(input("What is the second number?"))

    if user_operation == "addition" or user_operation == "add":
        print(user_first_number + user_second_number)

    elif user_operation == "subtraction" or user_operation == "subtract":
        print(user_first_number - user_second_number)

    elif user_operation == "multiplication" or user_operation == "multiply":
        print(user_first_number * user_second_number)

    elif user_operation == "division" or user_operation == "divide":
        print(user_first_number / user_second_number)

    else:
        print("Invalid input!")

    user_input = input("Would you like to continue?")

    if user_input == "No" or user_input == "no":
        print("Wrong answer.")

    elif user_input == "Yes" or user_input == "yes":
        print("Correct")

    else:
        print("Invalid input!")











