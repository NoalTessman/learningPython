import plotly.express as pf
import pandas as pd
def graphData():
    df = pd.read_csv("./quakes2.csv")
    fig = pf.scatter(df, x = "Quake Number",y = "Magnitude", title = "Earthquakes above 4 Magnitude after September",hover_data=['Location'])
    fig.show()
graphData()