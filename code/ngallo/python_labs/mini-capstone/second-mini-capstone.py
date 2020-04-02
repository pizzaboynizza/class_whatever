# imports functions 

from bs4 import BeautifulSoup
import requests 
import csv
from datetime import datetime
import pandas as pd
from html.parser import HTMLParser
import webbrowser

# function to get weather from Mount Hood Meadows, display the location in which it is geting the data from, and the returns a table.
def mount_hood():
    ## problem experienced on 03/13 - website URL changed from last night to today. 
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=45.3735&lon=-121.6956#.XmvkpKhKhEY")
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast")
    forecast_items = seven_day.find_all(class_="tombstone-container")
    tonight = forecast_items[0]
    period = tonight.find(class_="period-name").get_text()
    short_desc = tonight.find(class_="short-desc").get_text()
    temp = tonight.find(class_="temp").get_text()
    period_tags = seven_day.select(".tombstone-container .period-name")
    periods = [pt.get_text() for pt in period_tags]
    short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
    temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
    descs = [d["title"] for d in seven_day.select(".tombstone-container img")]  
    webbrowser.open("https://www.google.com/maps/search/45.34927%C2%B0N+121.68163%C2%B0W?sa=X&ved=2ahUKEwiH_N2zj5joAhXSoFsKHZR0Bq4Q8gEwAHoECAMQAQ", new=0, autoraise=True)
    weather_for_mount_hood = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
    })

    # print(period)
    # print(short_desc)
    # print(temps)
    # print(tonight.prettify())
    print(weather_for_mount_hood)
    return weather_for_mount_hood


# function to get weather from Mount Saint Helens, display the location in which it is geting the data from, and the returns a table.
def mount_saint_helens():
    page = requests.get("https://forecast.weather.gov/MapClick.php?lat=46.1912&lon=-122.1944#.XmvkXahKhEY")
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(id="seven-day-forecast")
    forecast_items = seven_day.find_all(class_="tombstone-container")
    tonight = forecast_items[0]
    period = tonight.find(class_="period-name").get_text()
    short_desc = tonight.find(class_="short-desc").get_text()
    temp = tonight.find(class_="temp").get_text()
    period_tags = seven_day.select(".tombstone-container .period-name")
    periods = [pt.get_text() for pt in period_tags]
    short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
    temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
    descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
    webbrowser.open("https://forecast.weather.gov/MapClick.php?lat=46.2332&lon=-122.1845#.Xmv57qhKhEY", new=0, autoraise=True)
    weather_for_mount_saint_helens = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc":descs
    })

    # print(period)
    # print(short_desc)
    # print(temps)
    # print(tonight.prettify())
    print(weather_for_mount_saint_helens)
    # writes to CSV File 
    return weather_for_mount_saint_helens

# function to write this information to a CSV file. 
def write_to_csv(weather_for_mount_hood):
    with open('weather-data.csv', 'a', encoding = "utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([f"Here is the current time: {datetime.now()}"])
        writer.writerow([f"Here is the weather for Mount Hood: \n {weather_for_mount_hood}"])
        # writer.writerow([f"here is the weather for Mount Saint Helens: \n {weather_for_mount_saint_helens}"])
    print("complete")


# calls functions
weather_for_mount_hood = mount_hood()
# weather_for_mount_saint_helens = mount_saint_helens()
write_to_csv(weather_for_mount_hood)