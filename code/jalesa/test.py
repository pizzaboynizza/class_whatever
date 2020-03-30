import random

ball_courts = [ "24 Hour Fitness The Pearl 228", "Overlook Park", "Lloyd Athletic Club", "Wallace Park", "Couch Park", "Matt Dishman Community Center & Pool", "LA Fitness", "Dawson Park"]

user_1_input = input("what locations would you like to get a notification from?")




Alex = ("Overlook Park")
Skylar = list(random.choices(ball_courts))
Doja = list(random.choices(ball_courts))
Levi = list(random.choices(ball_courts))


s1 = set(user_1_input)
print("set user_input", s1)
s2 = set(Alex)
s3 = set(Skylar)
s4 = set(Doja)
s5 = set(Levi)

results_s2 = s1.intersection(s2)
# print(results_s2)