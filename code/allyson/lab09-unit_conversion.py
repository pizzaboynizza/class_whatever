

print("Welcome to my basic distance converter!")
print("I honestly frankensteined it from some of my old projects")
print("This converter can handle the following options at this time.")
print("Centimeters (cm), Inches (in), Meters (m), Feet (ft), Yards (y), Miles (mi), and Kilometers (k)")
dist=input("What is the distance?"  )
dist=int(dist)
if type(dist) == int:
    pass
else:
    print("Not a number")

distance = {
    "ft": 3.28084,
    "m": 1, 
    "mi": 1609,
    "k": 1000,
    "in": 39.37,
    "cm":100,
    "y": 1.094
}

v1=input('From what?  ')
v2=input('To what?  ')


if v1 == v2:
	print("These are the same units of measurement.")

pt1=float(dist*distance[v1])
#pt1=int(pt1)
pt2=float(pt1/distance[v2])
pt2=int(pt2)
print(f"{dist}{v1} is equal to {pt2}{v2}")

#mass=input('Do you want to see all conversions?'  )
#if mass == "yes":
    
#    print(f"{dist} {v1} is equal to {m} meters, {mi} miles, and {km} kilometers")
    
#elif mass == "no":
#    print('Have a nice day!')
    
#else:
#		print("LOLWUT?")

import random
import sys
eyes = [":",";","X","8","<:","<;"]
noses = ["^"," ","","o","-"]
mouths = ["D",")","(","P",">","*","$","|","/"]

face = ""
eye = random.choice(eyes)
nose = random.choice(noses)
mouth = random.choice(mouths)

face = eye + nose + mouth

for i in range (1):
    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)

    print(f"{eye}{nose}{mouth}")

print('p.s. I know my math is off.')