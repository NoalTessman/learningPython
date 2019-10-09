import requests
import json
import time
import csv
from datetime import datetime

mag = 4
earthquakeAPI = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2019-09-0&minmagnitude={mag}"

data = requests.get(earthquakeAPI)
dataJson = data.json()
#print(dataJson['features'][1]["properties"]["mag"])
#wtr = csv.writer(open (f'{dataJson["metadata"]["count"]}Quakes above magnitude {mag}', 'w'), delimiter=',', lineterminator='\n')
wtr = csv.writer(open (f'quakes', 'w'), delimiter=',', lineterminator='\n')

wtr.writerow(["Quake Number", "Location","Magnitude","Time"])
#Lists all quakes starting at 2019-09-0 until now and makes a csv displaying the data
def listAllQuakes():
    counter = 1
    for x in (dataJson["features"]):
        currTime = x["properties"]["time"]/1000
        convertedTime = datetime.fromtimestamp(currTime).strftime('%Y-%m-%d %H:%M:%S')
        print (x["properties"]["title"], counter, convertedTime)
        wtr.writerow([counter,x["properties"]["title"],x["properties"]["mag"],convertedTime])
        counter += 1
#print(dataJson["metadata"]["count"])    
x = True
listAllQuakes()
currentQuake = dataJson["metadata"]["count"]
def recordCurrentQuakes():
    while x == True:
        time.sleep(5)
        updatedQuakes = (dataJson["metadata"]["count"])
        print(updatedQuakes)
        if updatedQuakes > currentQuake:
            print(dataJson["properties"][updatedQuakes])
        currentQuake = updatedQuakes
