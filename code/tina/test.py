user = input("What is the temp: ")

a = int(user)

if a < 60:
    print("That's kind cold")
elif a < 70:
    print("Getting warmer")
elif a < 80:
    print("Summer is here")
elif a < 100:
    print("You need to move!")
else:
    print("We will never get here if i did this right")