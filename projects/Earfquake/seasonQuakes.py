import requests
import json
import time
import csv
from datetime import datetime
mag = 5
earthquakeAPI = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2017-02-0&endtime=2019-02-0&minmagnitude={mag}"

data = requests.get(earthquakeAPI)
dataJson = data.json()

#Earthquake object creator
class earthquake:
    magnitude = 0
    Month = 0
    Day = 0
    name = ""
    def __init__(self, Month, Day, magnitude):
        self.Month = Month
        self.Day = Day
        self.magnitude = magnitude
quakes = []    
#grab earthquake date and mag data
for quake in dataJson["features"]:   
    mag = quake["properties"]["mag"]
    Month = datetime.fromtimestamp(quake["properties"]["time"]/1000).strftime('%m')
    Day = datetime.fromtimestamp(quake["properties"]["time"]/1000).strftime('%d')
    name = quake["properties"]["place"]
    quakes.append(earthquake(Month, Day, mag))

#put that data into earthquake object
#create winter, summer, spring, and Fall arrays to seperate objects into with dates.
Spring, Summer, Winter, Fall=([] for i in range(4))
for quake in quakes:
    currMonth = int(quake.Month)
    if currMonth == 12 or currMonth == 1 or currMonth ==2:
        Winter.append(quake)
    elif currMonth == 3 or currMonth == 4 or currMonth == 5:
        Spring.append(quake)
    elif currMonth == 6  or currMonth == 7 or currMonth == 8:
        Summer.append(quake)
    elif currMonth == 9 or currMonth == 10 or currMonth == 11:
        Fall.append(quake)
#seperate each season object based on magnitude
Seasons = [Spring, Summer, Fall, Winter]
#graph using a bar graph with each season having a thing that seperates earthquakes based on magnitude.
wtr = csv.writer(open (f'seasonQuakes.csv', 'w'), delimiter=',', lineterminator='\n')
wtr.writerow(["Seasons"])
wtr.writerow([Seasons])