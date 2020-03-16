import webbrowser
import requests
import random
from notify_run import Notify

url = "https://www.yelp.com/search?find_desc=Basketball%20Courts&find_loc=Pearl%20District%2C%20Portland%2C%20OR"

# how do i make the user interact with the yelp page then return that information???
# webbrowser.open_new_tab(url)

# user opens yelp and choose what basketball courts to get a notification from.

ball_courts = [ "24 Hour Fitness The Pearl 228", "Overlook Park",  "North Park Blocks","Lloyd Athletic Club", "Wallace Park", "Couch Park", "Matt Dishman Community Center & Pool", "LA Fitness", "Dawson Park"]

user_1_input = input("what locations would you like to get a notification from?: ").split(",")
print("user_1_input", user_1_input)

# people who have already chosen locations

list_of_courts = []
# user_2_input = list(random.choices(ball_courts, k=2))
user_2_input = ["Wallace Park", "Dawson Park"]
print(user_2_input)
# user_3_input = list(random.choices(ball_courts, k=4))
user_3_input = ["LA Fitness", "Dawson Park"]

print(user_3_input)
user_4_input = list(random.choices(ball_courts, k=2))
user_5_input = list(random.choices(ball_courts))

 # loop through lists and figure out matches if matches is 0 then nothing if it is 1,2 or more pick highest ranking one.
def location():
    s1 = set(user_1_input)
    s2 = set(user_2_input)
    s3 = set(user_3_input)
    # s4 = set(user_4_input)
    # set1 = s1.intersection(s2)
    # print(list(set1))
    results_sets = s1.intersection(s3)
    final = list(results_sets)
    print("final", final)
location()

s1.intersection(s2,s3, s4)
    

            
      

#     for x in user_3_input:
#         if x in user_1_input:
#             list_of_courts.append(x)
#             print(x)
#             return
#     for x in user_4_input:
#         if x in user_1_input:
#             list_of_courts.append(x)
#             print(x)
#             return
#     for x in user_5_input:
#         if x in user_1_input:
#             list_of_courts.append(x)
#             print(x)
#             return
# print(locations(x))
    
         

    

# I am filtering ppl who have already chosen a location with the locations I have chosen.









# After you filter by location; filter by day and time the users have chosen.
# put it into an if statement.



                    # NOTES
# if we have the same location that will be made into one list. 
# from that list:
#     filter the users by time.
