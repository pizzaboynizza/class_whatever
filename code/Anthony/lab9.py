

# VERSION 

distance = int(input("Enter Distance: "))

original_units = input("Enter starting units: ")
if original_units == 'mi':
    value = distance * 1609.34
if original_units == 'ft':
    value = distance * 0.3048
if original_units == 'km':
    value = distance * 1000
if original_units == 'inches':
    value = distance *0.0254
if original_units == 'yards':
    value = distance * 0.9144
if original_units == "meters":
    value = distance * 1
print(value)
   

new_units = input("Enter units to be converted to: ")
if new_units == 'mi':
    new_value =  value * 1609.34
if new_units == 'ft':
    new_value = value * 0.3048
if new_units == "km":
    new_value == value * 1000
if new_units == "meters":
    new_value = value * 1
if new_units == "yards":
    new_value = value * 0.9144
if new_units == "inches":
    new_value = value * 0.0254


print(float(new_value))

