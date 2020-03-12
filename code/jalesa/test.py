from notify_run import Notify
import webbrowser
import requests
import random


notify = Notify(endpoint="https://mail.google.com/mail/u/0/#inbox")
# notify = Notify(endpoint="https://notify.run/p115j44S8CcVHt73")


url = "https://www.yelp.com/search?find_desc=Basketball%20Courts&find_loc=Pearl%20District%2C%20Portland%2C%20OR"



# user opens yelp and choose what basketball courts to get a notification from.

ball_courts = [ "24 Hour Fitness The Pearl 228", "Overlook Park", "Lloyd Athletic Club", "Wallace Park", "Couch Park", "Matt Dishman Community Center & Pool", "LA Fitness", "Dawson Park"]

# implement while True loop when im done to avoid spaces.
user_1_input = input("what locations would you like to get a notification from?: ").split(",")
print("user_1_input", user_1_input)



list_of_courts = []
Alex = list(random.choices(ball_courts))
Skylar = list(random.choices(ball_courts))
Doja = list(random.choices(ball_courts))
Levi = list(random.choices(ball_courts))

 
def location():
    s1 = set(user_1_input)
    s2 = set(Alex)
    s3 = set(Skylar)
    s4 = set(Doja)
    s5 = set(Levi)
   
  
    if s1.intersection(s2):
         results_s2 = s1.intersection(s2)
         notify.send(f"Alex is on their way to {results_s2}")
         print("results_s2", list(results_s2))
    elif s1.intersection(s3):     
         results_s3 = s1.intersection(s3)
         notify.send(f"Skylar is on their way to {results_s3}")
         print("results_s3", list(results_s3))
    elif s1.intersection(s4):
         results_s4 = s1.intersection(s4)
         notify.send(f"Doja is on their way to {results_s4}")
         print("results_s4",list(results_s4))
    elif s1.intersection(s5):
         results_s5 = s1.intersection(s5)
         notify.send(f"Levi is on their way to {results_s5}")
         print("results_s5",list(results_s5))
location()

        #   Overlook Park,Wallace Park,LA Fitness  
      

