# import secrets
import webbrowser
import requests
import random

# url = "https://www.yelp.com/search?find_desc=24+Hour+Fitness&find_loc=Pearl+District%2C+Portland%2C+OR&ns=1"

# webbrowser.open_new_tab(url)

user_1_days = []
user_2_days = []

user_1_input = [input("what days would like to attend the gym?: ")]
print(user_1_input)
user_2_input = random.choice("Sunday, Monday, Tuesday, Wednesday, Thursday, Friday")
print(user_2_input)

user_2_days.append(user_2_input)

# list object is not callable because my lists does not match
filtered = filter(user_1_input, user_2_days)
print(filtered)

for x in filtered:
    print("filtered days", x)
