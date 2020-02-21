'''
# Lab 11: Simple Calculator
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and 
division. Ask the user for an operator and each operand. Don't forget that `input` returns a `string`, which you can convert to 
a float using `float(user_input)` where `user_input` is the string you got from `input`. Below is some sample input/output.
```
> What is the operation you'd like to perform? +
> What is the first number? 5
> What is the second number? 12
> 5 + 12 = 17
```

## Version 2
Allow the user to keep performing operations until they say 'done'. Use `while True` and `break`. Below is some sample 
input/output.
```
> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye! 
```

## Version 3 (optional)
Allow the user to enter a full arithmetic expression and use [eval](https://docs.python.org/3/library/functions.html#eval) to 
evaluate it.
'''
import string
valid_operation = '+-*/'
# operation = input('What is the operation you\'d like to perform? ')
# while operation not in valid_operation or len(operation) > 1 :
#     print('Enter a valid operation.')
#     operation = input('What is the operation you\'d like to perform? ')

# while True:
#     first_number = input('What is the first number? ')
#     valid_number = False
#     while not valid_number:  # make sure they enter digits with only 1 '.'.
#         for char in first_number:
#             if char not in string.digits + '.' or first_number.count('.') > 1:
#                 print('Enter a valid number.')
#                 first_number = input('What is the first number? ')
#                 break
#         else:
#             valid_number = True

#     second_number = input('What is the second number? ')
#     valid_number = False
#     while not valid_number:  # make sure they enter digits with only 1 '.'.
#         for char in second_number:
#             if char not in string.digits + '.' or second_number.count('.') > 1:
#                 print('Enter a valid number.')
#                 second_number = input('What is the second number? ')
#                 break
#         else:
#             valid_number = True

#     if operation == '+':
#         result = float(first_number) + float(second_number)    
#     elif operation == '-':
#         result = float(first_number) - float(second_number)
#     elif operation == '*':
#         result = float(first_number) * float(second_number)
#     else:
#         result = float(first_number) / float(second_number)

#     print(f'{first_number} {operation} {second_number} = {result}')
#     operation = input('What is the operation you\'d like to perform? ')
#     if operation == 'done':
#         break
#     while operation not in valid_operation or len(operation) > 1:
#         print('Enter a valid operation.')
#         operation = input('What is the operation you\'d like to perform? ')

# print('Bye!')

expression = input('Enter the arithmatic expression you\'d like to perform: ')
while True:
    valid_expression = False
    while not valid_expression: #make sure they enter digits and whitespace and only 1 '+-*/'.
        for char in expression:
            if char not in (string.digits + string.whitespace + valid_operation + '.') or expression.count('+') > 1 or expression.count('-') > 1 or expression.count('*') > 1 or expression.count('/') > 1:
                print('Enter a valid arithmatic expression.')
                expression = input('Enter the arithmatic expression you\'d like to perform: ')
                break
        else:
            valid_expression = True

    result = eval(expression)

    print(f'{expression} = {result}')
    expression = input('Enter the arithmatic expression you\'d like to perform: ')
    if expression == 'done':
        break

print('Bye!')
