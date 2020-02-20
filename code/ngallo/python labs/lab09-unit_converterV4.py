userDistance = int(input("What is the distance? "))
userUnitsFrom = input("What units you'd like to convert FROM? ")
userUnitsTo = input("What units would you like to convert TO? ")

newUserDistance = userDistance * 0.3048

if userUnitsFrom == "feet":
    print(newUserDistance * 0.3048)

elif userUnitsFrom == "yards":
    print(newUserDistance * 0.9144)

elif userUnitsFrom == "inches":
    print(newUserDistance * 0.0254)

elif userUnitsFrom == "miles":
    print(newUserDistance * 1609.34)

elif userUnitsFrom == "meters":
    print(newUserDistance * 1)

elif userUnitsFrom == "kilometers":
    print(newUserDistance * 1000)

else:
    print("error somewhere")

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m