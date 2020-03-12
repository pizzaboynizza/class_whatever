
# count_to_date & count_from_date

# from datetime import *
import datetime
# import calendar
# import time
from pytz import timezone   ################ IS THIS BEING USED?!?!?!?!

today = datetime.date.today()
weekday = datetime.date.weekday(today)
# months = ['january','february','march','april','may','june','july','august','september','october','november','december']
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


# print(f"Today is month {today.month} day {today.day} of {today.year}")

if today.month == 1:
  # print(months[0])
  print("Today's date:", months[0], today.day, today.year)  # Jan
elif today.month == 2:
  # print(months[1])
  print("Today's date:", months[1], today.day, today.year)  # Feb
elif today.month == 3:
  # print(months[2])
  print("Today's date:", months[2], today.day, today.year)  # Ma
elif today.month == 4:
  # print(months[3])
  print("Today's date:", months[3], today.day, today.year)  # Apr
elif today.month == 5:
  # print(months[4])
  print("Today's date:", months[4], today.day, today.year)  # May
elif today.month == 6:
  # print(months[5])
  print("Today's date:", months[5], today.day, today.year)  # June
elif today.month == 7:
  # print(months[6])
  print("Today's date:", months[6], today.day, today.year)  # July
elif today.month == 8:
  # print(months[7])
  print("Today's date:", months[7], today.day, today.year)  # Aug
elif today.month == 9:
  # print(months[8])
  print("Today's date:", months[8], today.day, today.year)  # Sept
elif today.month == 10:
  # print(months[9])
  print("Today's date:", months[9], today.day, today.year)  # Oct
elif today.month == 11:
  # print(months[10])
  print("Today's date:", months[10], today.day, today.year)  # Nov
elif today.month == 12:
  # print(months[11])
  print("Today's date:", months[11], today.day, today.year)  # Dec



if weekday == 0:
  print("today's weekday is", weekdays[0])  # Monday
elif weekday == 1:
  print("today's weekday is", weekdays[1])  # Tuesday
elif weekday == 2:
  print("today's weekday is", weekdays[2])  # Wednesday
elif weekday == 3:
  print("today's weekday is", weekdays[3])  # Thursday
elif weekday == 4:
  print("today's weekday is", weekdays[4])  # Friday
elif weekday == 5:
  print("today's weekday is", weekdays[5])  # Saturday
elif weekday == 6:
  print("today's weekday is", weekdays[6])  # Sunday


# I want it to print Tue Mar 10


print("Current year: ", datetime.date.today().strftime("%Y"))


# Dates that are always presented to the user: Memorial Day, 4th of July, Labor Day, Thanksgiving, Christmas Day, NYE

memorial = datetime.date(today.year,5,25)
print(memorial)
memorial_weekday_index = datetime.date.weekday(memorial)
print("weekday index: ", memorial_weekday_index)
memorial_weekday = weekdays[memorial_weekday_index]
print("Weekday: ", memorial_weekday)
count_to_mem = memorial - today
# print(type(count_to_mem))  # <class 'datetime.timedelta'>
print("days until Memorial Day 2020: ", count_to_mem)
print(f"This year Memorial Day is {memorial_weekday}, {months[4]} 25")

the_fourth = datetime.date(today.year,7,4)
print(the_fourth)
fourth_weekday_index = datetime.date.weekday(the_fourth)
print("weekday index: ", fourth_weekday_index)
fourth_weekday = weekdays[fourth_weekday_index]
print("Weekday: ", fourth_weekday)
count_to_fourth = (the_fourth) - today
# print(type(count_to_fourth))  # <class 'datetime.timedelta'>
print("days until 4th of July 2020: ", count_to_fourth)
print(f"This year the 4th of July is {fourth_weekday}, {months[6]} 4")

labor = datetime.date(today.year,9,7)
print(labor)
labor_weekday_index = datetime.date.weekday(labor)
print("weekday index: ", labor_weekday_index)
labor_weekday = weekdays[labor_weekday_index]
print("Weekday: ", labor_weekday)
count_to_labor = labor - today
# print(type(count_to_labor))  # <class 'datetime.timedelta'>
print("days until Labor Day 2020: ", count_to_labor)
print(f"This year Labor Day is {labor_weekday}, {months[8]} 7")

thanksgiving = datetime.date(today.year,11,26)
print(thanksgiving)
tgiving_weekday_index = datetime.date.weekday(thanksgiving)
print("weekday index: ", tgiving_weekday_index)
tgiving_weekday = weekdays[tgiving_weekday_index]
print("Weekday: ", tgiving_weekday)
count_to_tgiving = thanksgiving - today
# print(type(count_to_tgiving))  # <class 'datetime.timedelta'>
print("days until Thanksgiving Day 2020: ", count_to_tgiving)
print(f"This year Thanksgiving Day is {tgiving_weekday}, {months[10]} 26")

xmas = datetime.date(today.year,12,25)
print(xmas)
xmas_weekday_index = datetime.date.weekday(xmas)
print("weekday index: ", xmas_weekday_index)
xmas_weekday = weekdays[xmas_weekday_index]
print("Weekday: ", xmas_weekday)
count_to_xmas = xmas - today
# print(type(count_to_xmas))  # <class 'datetime.timedelta'>
print("days until Christmas Day 2020: ", count_to_xmas)
print(f"This year Christmas Day is {xmas_weekday}, {months[11]} 25")

nye = datetime.date(today.year,12,31)
print(nye)
nye_weekday_index = datetime.date.weekday(nye)
print("weekday index: ", nye_weekday_index)
nye_weekday = weekdays[nye_weekday_index]
print("Weekday: ", nye_weekday)
count_to_nye = nye - today
# print(type(count_to_nye))  # <class 'datetime.timedelta'>
print("days until New Year's Eve 2020: ", count_to_nye)
print(f"This year NYE is {nye_weekday}, {months[11]} 31")



# put this in a loop
# new_date = input("Do you want to add a countdown or count from? (no, down, from) ")
# if new_date == 'down':
#   print
# elif new_date == 'from':
#   print
# elif new_date == 'no':
#   print("You have completed your counters. Add or remove at anytime.")
# else:
#   print("Invalid input.")


# REMOVE A COUNTER option
# convert days to weeks

# days_to = 
# days_from = 