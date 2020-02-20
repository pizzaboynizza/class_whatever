print("Welcome to Mr. Measurement Converter!")
user_units = input("Which units would you like to convert from?\n1.feet 2.miles 3.kilometers 4.yards 5.inches\n> ")

if user_units == "1":
    unit_fill = "ft"
    user_distance = input("What is the distance in feet?")
    distance_meters = float(user_distance) * .3048
   
elif user_units == "2":
    unit_fill = "mi"
    user_distance = input("What is the distance in miles?")
    distance_meters = float(user_distance) * 1609.34
   

elif user_units == "3":
    unit_fill = "km"
    user_distance = input("What is the distance in kilometers?")
    distance_meters = float(user_distance) * 1000

elif user_units == "4":
    unit_fill = "yd"
    user_distance = input("What is the distance in yards?")
    distance_meters = float(user_distance) * .9144

elif user_units == "5":
    unit_fill = "in"
    user_distance = input("What is the distance in inches?")
    distance_meters = float(user_distance) * .0254


else:
    print("Sorry, try again!")
    quit()

output_units = input("Which units would you like to convert to?\n1.feet 2.miles 3.kilometers 4.yards 5.inches\n> ")

if output_units == "1":
    result_unit_fill = "ft"
    distance = float(distance_meters) /.3048
   
elif output_units == "2":
    result_unit_fill = "mi"
    distance= float(distance_meters) / 1609.34
   

elif output_units == "3":
    result_unit_fill = "km"
    distance = float(distance_meters) / 1000

elif output_units == "4":
    result_unit_fill = "yd"
    distance = float(distance_meters) / .9144

elif output_units == "5":
    result_unit_fill = "in"
    distance = float(distance_meters) / .0254

else:
    print("Sorry, try again!")
    quit()


results_abbrev = round(distance, 3)

print(f"{user_distance} {unit_fill} is {results_abbrev} {result_unit_fill}.")
