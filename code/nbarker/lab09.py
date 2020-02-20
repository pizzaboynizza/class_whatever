'''
Nick Barker
2/19/2020
Full Stack Day
'''


print("Welcome to the Big Unit Converter!")

'''
fdistance = int(input("Please enter your distance, in feet, it has to be in FEET!"))
print(f"{fdistance} feet! Wow!!")

#okay, we have the feet!  And the excitement that comes with a successfull measurment!

mdistance = fdistance * .3048
print(f"BRO! That's like {mdistance} meters!!!")

#part 1 done! with the added excitement!
'''

#part 2 allow the user to also enter the units, depending on the units, convert the distance to meters, we will allow feet, miles, meters, and kilometers.

'''
coeff = int(input("Lets convert your measurement! All I need is the distance, we will enter units next! "))
print(f"{coeff}, great!")
units = input("Okay! Now we need your unit....s ;-) ")



#This is the working Code for V 2/3
if units == "ft":
    print(f"{coeff} feet is about {coeff * .3048} m")
elif units == "mi":
    print(f"{coeff} miles is about {coeff * 1609.34} m")
elif units == "km":
    print(f"{coeff} kilometers is about {coeff * 1000} m")
elif units == "yd":
    print(f"{coeff} yards is about {coeff * .9144} m")
elif units == "in":
    print(f"{coeff} inches is about {coeff * .0254} m")
elif units == "m":
    print(f"{coeff} m is about {coeff} m")
else:
    print("Thank you for your time!")
'''

#this is where V4 Starts

coeff = int(input("Lets get your measurement! All we need is the distance, we will enter input and output units next! "))
print(f"{coeff}, Great! ")

uin = input("Now what units are we INputting? ft, mi, m, or km?")
print(f"Okay, great! {uin} it is!")

uout = input("Lastly, which units are we OUTputting? (which units would you like to end with?) ft, mi, m, or km?")
print(f"Okay, {uout} coming up!")

if uin == "m" and uout == "m":
    print(f"{coeff} meters!")
elif uin == "m" and uout == "km":
    print(f"{coeff * 1000} kilometers!")
elif uin == "m" and uout == "mi":
    print(f"{coeff / 1609} miles!")
elif uin == "m" and uout == "ft":
    print(f"{coeff * .3048} feet!")
elif uin == "km" and uout == "km":
    print(f"{coeff} kilometers!!")
elif uin == "km" and uout == "m":
    print(f"{coeff * 1000} meters!!!")
elif uin == "km" and uout == "ft":
    print(f"{coeff * 3280.84} feet!")
elif uin == "km" and uout == "mi":
    print(f"{coeff * .6213712} miles!")
elif uin == "ft" and uout == "km":
    print(f"{coeff * .0003048} kiometers!")
elif uin == "ft" and uout == "m":
    print(f"{coeff * .3048} meters!")
elif uin == "ft" and uout == "ft":
    print(f"{coeff} feet!")
elif uin == "ft" and uout == "mi":
    print(f"{coeff / 5280} miles!")
elif uin == "mi" and uout == "km":
    print(f"{coeff * 1.609} kilometers!")
elif uin == "mi" and uout == "m":
    print(f"{coeff * 1609} meters!")
elif uin == "mi" and uout == "ft":
    print(f"{coeff * 5280} feet!")
elif uin == "mi" and uout == "mi":
    print(f"{coeff} miles!")
else: 
    print("Unlawful Entry! Must be entered mi, ft, m, or km! Self Destruct!")