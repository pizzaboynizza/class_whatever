'''
1. Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048

2. Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

3. Add support for yards, and inches

4. Now we'll ask the user for the distance, the starting units, and the units to convert to.
(if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.
Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units
'''

#Converting To Meters
unit_from = input("What is the unit (ft, mi, m, km, yd, in) you want to convert to meters? ")
distance = int(input("What is the distance? "))
#conversion formula to meters
conversion = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}
x = conversion[unit_from] * distance
print(f"That is {x} meters.")


#Converting From And To Anything
unit_from = input("What is the unit (ft, mi, m, km, yd, in) you want to convert? ")
distance = float(input("What is the distance? "))
convert_to = input("What is the unit (ft, mi, m, km, yd, in) you want to convert to? ")
conversion = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
}
x = conversion[unit_from] * distance
#need to convert from meters but not to
if unit_from == 'mi' and convert_to == 'km':
  print(x / conversion[convert_to])
elif unit_from == 'mi' and convert_to == 'ft':
  print(x / conversion[convert_to])
elif unit_from == 'mi' and convert_to == 'yd':
  print(x / conversion[convert_to])
elif unit_from == 'mi' and convert_to == 'in':
  print(x / conversion[convert_to])
elif unit_from == 'ft' and convert_to == 'km':
  print(x / conversion[convert_to])
elif unit_from == 'ft' and convert_to == 'mi':
  print(x / conversion[convert_to])
elif unit_from == 'ft' and convert_to == 'yd':
  print(x / conversion[convert_to])
elif unit_from == 'ft' and convert_to == 'in':
  print(x / conversion[convert_to])
elif unit_from == 'km' and convert_to == 'ft':
  print(x / conversion[convert_to])
elif unit_from == 'km' and convert_to == 'mi':
  print(x / conversion[convert_to])
elif unit_from == 'km' and convert_to == 'yd':
  print(x / conversion[convert_to])
elif unit_from == 'km' and convert_to == 'in':
  print(x / conversion[convert_to])
elif unit_from == 'yd' and convert_to == 'ft':
  print(x / conversion[convert_to])
elif unit_from == 'yd' and convert_to == 'mi':
  print(x / conversion[convert_to])
elif unit_from == 'yd' and convert_to == 'km':
  print(x / conversion[convert_to])
elif unit_from == 'yd' and convert_to == 'in':
  print(x / conversion[convert_to])
elif unit_from == 'in' and convert_to == 'ft':
  print(x / conversion[convert_to])
elif unit_from == 'in' and convert_to == 'mi':
  print(x / conversion[convert_to])
elif unit_from == 'in' and convert_to == 'km':
  print(x / conversion[convert_to])
elif unit_from == 'in' and convert_to == 'yd':
  print(x / conversion[convert_to])
else:
  print("Invalid input.")