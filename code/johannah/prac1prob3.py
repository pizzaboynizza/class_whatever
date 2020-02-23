#Write a function that returns True if a number within 10 of 100
user_input = []
def near_100(user_input):
  user_input = float(input("Enter a number to dtermine if it is within 10 and 100: "))
  if user_input >= 10 and user_input <= 100:
    print("True")
  else:
    print("False")
near_100(user_input)