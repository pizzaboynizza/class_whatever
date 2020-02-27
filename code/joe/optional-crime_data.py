# Lab : Crime Data
# Author : Joe

# Record ID, Report Date, Report Time, Major Offense Type, Address, Neighborhood, Police Precinct, Police District, X Coordinate,Y Coordinate

import csv

files = ["2011", "2012", "2013", "2014"]

for fname in files:
    csvfile = f"../../1 Python/data/crime_incident_data_{fname}.csv"

    fields = []

    common_crime_type = dict()
    crime_year = dict()

    with open(csvfile, "r") as crime_data:
        cd_reader = csv.reader(crime_data)
        fields = cd_reader.__next__() # .next() didn't work, even though it's supposed to?
        for row in cd_reader:
            # Crime types
            if row[3] in common_crime_type:
                common_crime_type[row[3]] += 1
            else:
                common_crime_type[row[3]] = 1
            # Crime years
            y = row[1].split("/")[-1]
            if y in crime_year:
                crime_year[y] += 1
            else:
                crime_year[y] = 1

    sorted_crime = list(common_crime_type.items())

    sorted_crime.sort(key=lambda tup: tup[1], reverse=True)

    print(f"{'*'*50}\nAccording to the database \"{csvfile.split('/')[-1]}\"...")

    # The specific most common crime type
    most_common_type = sorted_crime[0]
    print(f"\n\tThe most common crime is {most_common_type[0]}, with {most_common_type[1]} instances.")

    # The rarest crimes.
    least_common_type = sorted_crime[-1]
    print(f"\n\tThe rarest crime is {least_common_type[0]}, with {least_common_type[1]} instances.")

    # The year with the most crime.
    sorted_year = list(crime_year.items())
    sorted_year.sort(key=lambda tup: tup[1], reverse=True)
    most_crime_year = sorted_year[0]
    print(f"\n\tThe year with the most crime is {most_crime_year[0]}, with {most_crime_year[1]} crimes commited during that year.")