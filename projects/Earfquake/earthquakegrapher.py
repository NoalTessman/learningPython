import plotly.express as pf
import pandas as pd
def graphData():
    df = pd.read_csv("./quakes.csv")
    fig = pf.line(df, x = "Quake Number",y = "Magnitude", title = "Earthquakes above 4 Magnitude after September")
    fig.show()
graphData()