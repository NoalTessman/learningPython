import random
import plotly.io as pio

numarr = []
series = []
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
fig = {
    "data":[{"type":"bar",
    'x':series,
    'y':numarr}],
    "layout":{"title":{"text":"Perin Noise?"}}
}
pio.show(fig)
