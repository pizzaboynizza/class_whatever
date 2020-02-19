'''
# Lab 9: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

## Version 1

Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the 
output in meters by **multiplying the input distance by 0.3048**. Below is some sample input/output.

```
> what is the distance in feet? 12
> 12 ft is 3.6576 m
```

## Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are 
feet, miles, meters, and kilometers.

```
1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
```

Below is some sample input/output:

```
> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
```

## Version 3

Add support for yards, and inches.

```
1 yard is 0.9144 m
1 inch is 0.0254 m
```

## Version 4

Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting 
from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 
foot is 1 foot, etc).



|  | ft  | mi  | m  | km  |
|---|----|----|----|---|
|ft|1||0.3048||
|mi||1|1609.34||
|m|1/0.3048|1/1609.34|1|1/1000|
|km|||1000|1|

But instead of filling out that matrix, and checking for each pair of units (`if from_units == 'mi' and to_units == 'km'`), we 
can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first 
convert from the input units **_to_** meters, then convert **_from_** meters to the output units.



Below is some sample input/output:

```
> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi
```
'''
import string
units_org = input('What are the units of the distance? ')
valid_units = {'m', 'ft', 'km', 'mi', 'yd', 'in'}
while units_org not in valid_units:#make sure they enter a valid unit
    print('Enter a valid unit.')
    units_org = input('What are the units of the distance? ')

units_final = input('What are the units to convert to? ')
while units_final not in valid_units and units_final != units_org:#make sure they enter a valid unit
    print('Enter a valid unit.')
    units_final = input('What are the units to convert to? ')

distance_units_org = input(f'What is the distance in {units_org}? ')
valid_distance = False
num_dot = 0
while not valid_distance:#make sure they enter a digit
    for i in distance_units_org:
        if i == '.':
            num_dot += 1
        if i not in string.digits + '.' or num_dot > 1:
            print('Enter a valid distance.')
            distance_units_org = input(f'What is the distance in {units_org}? ')
            num_dot = 0
            break
    else:
        valid_distance = True

distance_m = float(distance_units_org)
if units_org == 'ft':# this converts units_org to m
    distance_m *= 0.3048
elif units_org == 'km':
    distance_m *= 1000
elif units_org == 'mi':
    distance_m *= 1609.34
elif units_org == 'yd':
    distance_m *= 0.9144
elif units_org == 'in':
    distance_m *= 0.0254

distance_final = distance_m
if units_final == 'ft':#this converts from m to units_final
    distance_final /= 0.3048
elif units_final == 'km':
    distance_final /= 1000
elif units_final == 'mi':
    distance_final /= 1609.34
elif units_final == 'yd':
    distance_final /= 0.9144
elif units_final == 'in':
    distance_final /= 0.0254

if round(distance_final, 4) % 1 == 0: #this checks if distance_final is close to a whole number
    print(f'{distance_units_org} {units_org} is {int(round(distance_final, 4))} {units_final}')
else:
    print(f'{distance_units_org} {units_org} is {distance_final} {units_final}' )