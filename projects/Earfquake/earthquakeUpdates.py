import requests
import json
from datetime import datetime
earthquakeAPI = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2019-09-0&minmagnitude=3"

data = requests.get(earthquakeAPI).json()
print(data['features'][1]["properties"]["mag"])
counter = 1
for x in (data["features"]):
    currTime = x["properties"]["time"]/1000
    convertedTime = datetime.fromtimestamp(currTime).strftime('%Y-%m-%d %H:%M:%S')
    print (x["properties"]["title"], counter, convertedTime)
    counter += 1
print (len(data["features"]))