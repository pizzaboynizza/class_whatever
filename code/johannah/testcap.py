# subtracting dates with diff timezones
# (future date in diff time zone) - today with no time

import datetime
import pytz

today = datetime.date.today()
today_time = datetime.datetime.today()
user_input = input("What timezone would you like to utilize? ")
user_tz_current = datetime.datetime.now(pytz.timezone(user_input))
print(f"In {user_input} the current date, time, and UTC is {user_tz_current}")
user_chosen_tz = pytz.timezone(user_input)
time_difference = user_tz_current - today_time
print("The time difference is", time_difference)