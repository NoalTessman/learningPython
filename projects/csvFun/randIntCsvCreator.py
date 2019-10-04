import random
import csv
import plotly.express as px
def randGen():
    y = random.randint(1,1001)
    return  y
arr=[]
for x in range(100):
    arr.append(randGen())

print(arr)


wtr = csv.writer(open ('out.csv', 'w'), delimiter=',', lineterminator='\n')
wtr.writerow(["series", "number"])
counter = 0
#arr.sort()
for x in arr:
    wtr.writerow([counter,x])
    counter += 1
#Overwrites previous csv file and keeps the same name