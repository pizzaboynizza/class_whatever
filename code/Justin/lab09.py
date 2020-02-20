
user_input = float(input("What is the distance?"))

user_unit = input("What is the unit?")

if user_unit == "feet":
    print(user_input * 0.3048)

elif user_unit == "miles":
    print(user_input * 1609.34)

elif user_unit == "meters":
    print(user_input * 1)

elif user_unit == "kilometers":
    print(user_input * 1000)

elif user_unit == "yard":
    print(user_input * 0.9144)

elif user_unit == "inch":
    print(user_input * 0.0254)

else:
    print("Invalid input")

user_distance = float(input("What is the distance?"))

user_inputunit = input("What is the input unit?")

user_outputunit = input("What is the output unit?")

if user_inputunit == "feet":
    user_inputunit2 = 1/0.3048

elif user_inputunit == "miles":
    user_inputunit2 = 1/1609.34

elif user_inputunit == "kilometers":
    user_inputunit2 = 1/1000

if user_outputunit == "feet":
    user_outputunit2 = user_inputunit2 * 0.3048

elif user_outputunit == "miles":
    user_outputunit2 = user_inputunit2 * 1609.34

elif user_outputunit == "kilometers":
    user_outputunit2 = user_inputunit2 * 1000

else:
    print("invalid input")

print(int(user_distance), user_inputunit, 'is', int(user_inputunit2), user_outputunit)







