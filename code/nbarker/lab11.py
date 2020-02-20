'''
Nick Barker
Lab11
2/19/2020

Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.
'''

#Calculator
#Variables - opera, num1, num2
#User input will need to be float
#input returns a string which you can make into a float using float (user_input) where user_input is the string you got from input.

print("Welcome to the Calculatador!")

game_in_session = "yes"
#this will make the loop run!

while game_in_session == "yes":
#this was brutal to remember
    opera = (input("Which calculator operation would you care to perform today? Don't worry, numbers are next! Please enter +, -, *, or /"))

    print(f"Okay, {opera} is my best operation!")

    num1 = float(input("Please enter your starting number!"))

    num2 = float(input("Please enter your other number, this will be the divisor or the amount subtracted if / or - "))

    if opera == "/":
        print(num1/num2)
    elif opera == "-":
        print(num1 - num2)
    elif opera == "+":
        print(num1+ num2)
    elif opera == "*":
        print(num1 * num2)
    #awesome
    game_in_session = input("Would you like another calculation? I'm like totally way faster than you, silly human!").lower()
else: 
    print("Goodbye!")
