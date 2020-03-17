
# count_to_date & count_from_date

# from datetime import *
import datetime
# from pytz import timezone
import pytz

today = datetime.date.today()  # <class 'datetime.date'>
weekday = datetime.date.weekday(today)  # PRINTS INDEX
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

# Today's Day of Week:
if weekday == 0:
  day_of_week = weekdays[0]   # Monday
elif weekday == 1:
  day_of_week = weekdays[1]   # Tuesday
elif weekday == 2:
  day_of_week = weekdays[2]   # Wednesday
elif weekday == 3:
  # print(type(weekdays[3]))   # <class 'str'>
  day_of_week = weekdays[3]   # Thursday
elif weekday == 4:
  day_of_week = weekdays[4]   # Friday
elif weekday == 5:
  day_of_week = weekdays[5]   # Saturday
elif weekday == 6:
  day_of_week = weekdays[6]   # Sunday
print(f"Today is {day_of_week}, {today.strftime('%B')} {today.strftime('%d')}, {today.strftime('%Y')}")  # Thursday, March 12, 2020



def holidays():     # Dates/Holidays that are always presented to the user

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

holidays()


# TIMEZONES
# kgl_time = datetime.datetime.now(pytz.timezone('Africa/Kigali'))  # 2020-03-13 03:11:58.309381+02:00     # datetime.datetime
# kgl_date = datetime.date.today(pytz.timezone('Africa/Kigali'))
# print(kgl_date)
for tz in pytz.all_timezones:
    print(tz)
# what is the date today in a different timezone?
# do you want to change your date to a different timezone?
user_input = input("What timezone would you like to utilize? ")
user_tz_current = datetime.datetime.now(pytz.timezone(user_input))
print(f"In {user_input} the current date, time, and UTC is {user_tz_current}")
user_chosen_tz = pytz.timezone(user_input)
# print(local.date(user_input))   # import arrow


file = open('pythoncap.txt','r')

counters = file.readlines()

while True:
  new_date = input("Do you want to add a countdown or count from/since, or remove one, or are you finished? (down, since, remove, finish) ")
  if new_date == 'down':
    print("WELCOME! What is the date you want to countdown to? ")
    year = int(input('Enter a year (format: yyyy): '))
    month = int(input('Enter a month (number): '))
    day = int(input('Enter a day (number): '))
    # time = 
    countdown = datetime.date(year, month, day)  # <class 'datetime.date'>
    count_to = countdown - today
    days_to = count_to.days
    weeks_to = (days_to) / 7
    weeks_until = round(weeks_to,2)
    new_date_weekday_index = datetime.date.weekday(countdown)
    new_date_weekday = weekdays[new_date_weekday_index]
    counters.append(f"It is {days_to} days (or approximately {weeks_until} weeks) until {new_date_weekday}, {countdown.strftime('%B')} {countdown.strftime('%d')}, {countdown.strftime('%Y')}\n")
    print(counters[-1])
    # file.write(f"It is {days_to} days (or approximately {weeks_until} weeks) until {new_date_weekday}, {countdown.strftime('%B')} {countdown.strftime('%d')}, {countdown.strftime('%Y')}\n")
  elif new_date == 'since':
    print("WELCOME! What is the date you want to count from/since? ")
    year = int(input('Enter a year (format: yyyy): '))
    month = int(input('Enter a month (number): '))
    day = int(input('Enter a day (number): '))
    count_from = datetime.date(year, month, day)
    count_since = today - (count_from)  # 71 days, 0:00:00
    days_since = count_since.days  # 71
    weeks_been = (days_since) / 7
    weeks_since = round(weeks_been,2)
    new_date_weekday_index = datetime.date.weekday(count_from)
    new_date_weekday = weekdays[new_date_weekday_index]
    counters.append(f"It has been {days_since} days (or approximately {weeks_since} weeks) since {new_date_weekday}, {count_from.strftime('%B')} {count_from.strftime('%d')}, {count_from.strftime('%Y')}\n")
    print(counters[-1])
    # file.write(f"It has been {days_since} days (or approximately {weeks_since} weeks) since {new_date_weekday}, {count_from.strftime('%B')} {count_from.strftime('%d')}, {count_from.strftime('%Y')}\n")
  elif new_date == 'remove':
    print(counters)
    line_remove = int(input("What line number do you want to delete?"))
    counters.pop(line_remove-1)
    # for line in file:
    #   if line.strip("\n") != "nickname_to_delete":
    #     file.write(line)
  elif new_date == 'finish':
    print("You have completed your counters. Come back to add or remove at anytime.")
    break
  else:
    print("Invalid input.")
    # how do I give a try again option to loop back thru if statement?

file = open('pythoncap.txt','w')
for item in counters:
  file.write(item)
file.close()


# REMOVE A COUNTER option


# days_to = 
# days_from = 