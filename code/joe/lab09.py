#Lab 9

units = ["ft", "mi", "m", "km", "yd", "in",
"feet", "foot", "miles", "mile", "meters", "meter", "kilometers", "kilometer", "yards", "yard", "inches", "inch"]

def getUnit(msg):
    ret = input(msg)
    while ret not in units:
        ret = input("Invalid units; please enter another: ")
    if ret == "feet" or ret == "foot":
        ret = "ft"
    elif ret == "miles" or ret == "mile":
        ret = "mi"
    elif ret == "meters" or ret == "meter":
        ret = "m"
    elif ret == "kilometers" or ret == "kilometer":
        ret = "km"
    elif ret == "yards" or ret == "yard":
        ret = "yd"
    elif ret == "inches" or ret == "inch":
        ret = "in"

    return ret

def getConv(unit):
    if unit == "ft":
        return 0.3048
    elif unit == "mi":
        return 1609.34
    elif unit == "km":
        return 1000.0
    elif unit == "yd":
        return 0.9144
    elif unit == "in":
        return 0.0254
    else:
        return 1.0

def getFloat(msg):
    try:
        result = float(input(msg))
        return result
    except ValueError:
        return getFloat("Must enter a number: ")

u_from = getUnit("Enter units to convert from: ")

u_to = getUnit("Enter units to convert to: ")

distance = getFloat("Please enter distance: ")

result = (distance * getConv(u_from)) / getConv(u_to)
result = round(result, 4)

print(f"\n{distance} {u_from} is {result} {u_to}.")