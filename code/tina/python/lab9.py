# Unit con
Unit = {
'feet': 0.3048,
'meters': 1,
'miles': 1609.34,
'kilo': 1000,
'yard': 0.9144,
'inch': 0.0254
}

for x in Unit:
    print(x)

while True:
    user = int(input("What is the Distance: "))
    unit1 = input("What Units: ")
    convert = input("Output Units: ")
    con = Unit[unit1] * (user) / Unit[convert]
    print(f"{user} {unit1} is ", con , f"{convert}")

    user1 = input("Again? ")
    if user1 not in ['yes','YES','y']:
        break


    



    


