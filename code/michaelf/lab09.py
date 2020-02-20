
distance_feet = input("What is the distance in feet?")

distance_meters = float(distance_feet) * .3048
results = str(distance_meters)
results_abbrev = results[0:5]
print(f"{distance_feet} ft is {results_abbrev} m.")
