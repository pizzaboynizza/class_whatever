"""
unit converter lab
    by: Matt

conversions:
1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
1 yd is 0.9144 m
1 in is 0.0254 m
"""
# dictionary for all values to convert input to meters
unit_store = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}

#asks user for input for distance in given unit type
num_in = int(input("What is the distance? "))
unit_in = input(f"""What is the input unit?
(must be "ft", "mi", "m", "km", "yd", or "in"): """)

#converts user input to meters and stores value
num_store = unit_store[unit_in] * num_in
int(num_store)

# asks user what distance unit they want to convert to, and converts from meters to output unit requested
unit_out = input("What is the output unit? ")
num_out = num_store / unit_store[unit_out]

print(f"{num_in} {unit_in} is {num_out} {unit_out}")