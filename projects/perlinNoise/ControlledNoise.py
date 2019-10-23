import random
import plotly.io as pio

numarr = []
series = []
def landGenerator():
    currNum = random.randint(1,101)
    for x in range(1000):
        y = random.randint(1,3)
        dice = random.randint(1,2)
        if dice == 1:
            currNum+=y
        elif dice == 2:
            currNum-=y
        numarr.append(currNum)
        series.append(x)
def smoothlaaaaaaaaaaaaaaaaaaaaand():
    for x in range(len(numarr)):
        if x > 0 and x < len(numarr)-1:
            numarr[x] = (numarr[x-1]+numarr[x+1]+numarr[x])/3
def landGrapher():
    fig = {
        "data":[{"type":"bar",
        'x':series,
        'y':numarr}],
    }
    pio.show(fig)
def generateLand():
    landGenerator()
    smoothlaaaaaaaaaaaaaaaaaaaaand()
    landGrapher()
generateLand()