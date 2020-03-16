
# count_to_date & count_from_date

# from datetime import *
import datetime
# import calendar
# import time
from pytz import timezone   ################ IS THIS BEING USED?!?!?!?!

today = datetime.date.today()  # <class 'datetime.date'>
weekday = datetime.date.weekday(today)  # PRINTS INDEX
# months = ['january','february','march','april','may','june','july','august','september','october','november','december']
# months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec']
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']



print("today's date is", today)  # 2020-03-12
print(f"today is {today.strftime('%B')} {today.strftime('%d')}, {today.strftime('%Y')}")  # March 12, 2020
# print("the day of the week today is", weekday)  # PRINTS INDEX


# print("today:", today)  # 2020-03-11


# print(f"Today is month {today.month} day {today.day} of {today.year}")
'''
date_today = []
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
'''


# Today's Weekday:
weekday_today = []
if weekday == 0:
  print("Today is a", weekdays[0])  # Monday
elif weekday == 1:
  print("Today is a", weekdays[1])  # Tuesday
elif weekday == 2:
  print("Today is a", weekdays[2])  # Wednesday
elif weekday == 3:
  print("Today is a", weekdays[3])  # Thursday
elif weekday == 4:
  print("Today is a", weekdays[4])  # Friday
elif weekday == 5:
  print("Today is a", weekdays[5])  # Saturday
elif weekday == 6:
  print("Today is a", weekdays[6])  # Sunday


# join date_today and weekday_today

# I want it to print Tue Mar 10


print("Current year: ", datetime.date.today().strftime("%Y"))



# Dates that are always presented to the user: Memorial Day, 4th of July, Labor Day, Thanksgiving, Christmas Day, NYE

memorial = datetime.date(2020,5,25)  # date of holiday
memorial_weekday_index = datetime.date.weekday(memorial)
memorial_weekday = weekdays[memorial_weekday_index]     # day of week holiday is on
count_to_mem = memorial - today
days_to_mem = count_to_mem.days
print("Memorial Day:")
print(f"This year Memorial Day is {memorial_weekday}, {memorial.strftime('%B')} {memorial.strftime('%d')}")
print(f"There are {days_to_mem} days until Memorial Day 2020")


the_fourth = datetime.date(2020,7,4)  # date of holiday
fourth_weekday_index = datetime.date.weekday(the_fourth)
fourth_weekday = weekdays[fourth_weekday_index]     # day of week holiday is on
count_to_fourth = (the_fourth) - today
days_to_fourth = (count_to_fourth).days
print("4th of July:")
print(f"This year the 4th of July is {fourth_weekday}, {the_fourth.strftime('%B')} {the_fourth.strftime('%d')}")
print(f"There are {days_to_fourth} days until the 4th of July 2020")


labor = datetime.date(2020,9,7)  # date of holiday
labor_weekday_index = datetime.date.weekday(labor)
labor_weekday = weekdays[labor_weekday_index]     # day of week holiday is on
count_to_labor = labor - today
days_to_labor = (count_to_labor).days
print("Labor Day:")
print(f"This year Labor Day is {labor_weekday}, {labor.strftime('%B')} {labor.strftime('%d')}")
print(f"There are {days_to_labor} days until Labor Day 2020")


thanksgiving = datetime.date(2020,11,26)  # date of holiday
tgiving_weekday_index = datetime.date.weekday(thanksgiving)
tgiving_weekday = weekdays[tgiving_weekday_index]     # day of week holiday is on
count_to_tgiving = thanksgiving - today
days_to_tgiving = (count_to_tgiving).days
print("Thanksgiving:")
print(f"This year Thanksgiving Day is {tgiving_weekday}, {thanksgiving.strftime('%B')} {thanksgiving.strftime('%d')}")
print(f"There are {days_to_tgiving} days until Thanksgiving Day 2020")


xmas = datetime.date(2020,12,25)  # date of holiday
xmas_weekday_index = datetime.date.weekday(xmas)
xmas_weekday = weekdays[xmas_weekday_index]     # day of week holiday is on
count_to_xmas = xmas - today
days_to_xmas = (count_to_xmas).days
print("Christmas Day:")
print(f"This year Christmas Day is {xmas_weekday}, {xmas.strftime('%B')} {xmas.strftime('%d')}")
print(f"There are {days_to_xmas} days until Christmas Day 2020")


nye = datetime.date(2020,12,31)  # date of holiday
nye_weekday_index = datetime.date.weekday(nye)
nye_weekday = weekdays[nye_weekday_index]     # day of week holiday is on
count_to_nye = nye - today
days_to_nye = (count_to_nye).days
print("NYE:")
print(f"This year NYE is {nye_weekday}, {nye.strftime('%B')} {nye.strftime('%d')}")
print(f"There are {days_to_nye} days until New Year's Eve 2020")




# put this in a loop
new_date = input("Do you want to add a countdown or count from/since? (no, down, from) ")
if new_date == 'down':
  print("WELCOME! What is the date you want to countdown to? ")
  year = int(input('Enter a year (format: yyyy): '))
  month = int(input('Enter a month (number): '))
  day = int(input('Enter a day (number): '))
  countdown = datetime.date(year, month, day)  # <class 'datetime.date'>
  count_to = countdown - today
  days_to = count_to.days
  weeks_to = (days_to) / 7
  weeks_until = round(weeks_to,2)
  # WHAT IS THE WEEKDAY?!?!
  print(f"It is {days_to} days (or approximately {weeks_until} weeks) until {countdown.strftime('%B')} {countdown.strftime('%d')}, {countdown.strftime('%Y')}")
elif new_date == 'from':
  print("WELCOME! What is the date you want to count from/since? ")
  year = int(input('Enter a year (format: yyyy): '))
  month = int(input('Enter a month (number): '))
  day = int(input('Enter a day (number): '))
  count_from = datetime.date(year, month, day)
  count_since = today - (count_from)  # 71 days, 0:00:00
  days_since = count_since.days  # 71
  weeks_been = (days_since) / 7
  weeks_since = round(weeks_been,2)
  # WHAT IS THE WEEKDAY?!?!
  print(f"It has been {days_since} days (or approximately {weeks_since} weeks) since {count_from.strftime('%B')} {count_from.strftime('%d')}, {count_from.strftime('%Y')}")
elif new_date == 'no':
  print("You have completed your counters. Come back to add or remove at anytime.")
else:
  print("Invalid input.")
  # how do I give a try again option to loop back thru if statement?


# REMOVE A COUNTER option


# days_to = 
# days_from = 