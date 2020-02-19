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

user = input("What is the Distance: ")
unit1 = input("What Units: ")
convert = input("Output Units: ")

con = Unit[unit1] * int(user) / Unit[convert]
print(con)


    



    


