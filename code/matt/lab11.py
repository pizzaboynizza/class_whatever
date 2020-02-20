"""
lab 11: Simple Calculator
    by: Matt Woodside

Version 2:
Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye! 

Version 3 (optional)
Allow the user to enter a full arithmetic expression and use eval to evaluate it.
"""
#Version 2
# while True:
#     operation_type = input("What is the operation you'd like to perform? ")
#     if operation_type == "done":
#         print("Goodbye.")
#         break
#     first_num = int(input("What is the first number? "))
#     second_num = int(input("What is the second number? "))
#     if operation_type in ["+", "add", "plus"]:
#         print(f"{first_num} {operation_type} {second_num} = ")
#         print(first_num + second_num)
#     elif operation_type in ["-", "subtraction", "subtract", "minus"]:
#         print(f"{first_num} {operation_type} {second_num} = ")
#         print(first_num - second_num)
#     elif operation_type in ["*", "multiply", "multiplication"]:
#         print(f"{first_num} {operation_type} {second_num} = ")
#         print(first_num * second_num)
#     elif operation_type in ["/", "divide", "division"]:
#         print(f"{first_num} {operation_type} {second_num} = ")
#         print(first_num / second_num)        



#Version 3
while True:
    user_maths = eval(input("Enter your maths expression: "))
    print(user_maths)