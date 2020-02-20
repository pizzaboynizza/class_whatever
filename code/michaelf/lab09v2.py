
print("Welcome to Mr. Meter! Convert your measurement to meters.")
user_units = input("Which units would you like to convert from?\n1.feet 2.miles 3.kilometers\n>")

if user_units == "1":
    distance_feet = input("What is the distance in feet?")
    distance_meters = float(distance_feet) * .3048
    results = str(distance_meters)
    results_abbrev = results[0:5]
    print(f"{distance_feet} ft is {results_abbrev} m.")

elif user_units == "2":
    distance_miles = input("What is the distance in miles?")
    distance_meters = float(distance_miles) * 1609.34
    results = str(distance_meters)
    results_abbrev = results[0:5]
    print(f"{distance_miles} mi is {results_abbrev} m.")

elif user_units == "3":
    distance_kilometers = input("What is the distance in kilometers?")
    distance_meters = float(distance_kilometers) * 1000
    results = str(distance_meters)
    results_abbrev = results[0:5]
    print(f"{distance_kilometers} km is {results_abbrev} m.")
else:
    print("Sorry, try again!")
