import plotly.express as px
import pandas as pd
def graphData():
    df = pd.read_csv("./seasonQuakes.csv")
    fig = px.bar(df,x = "Seasons", y = "Amount of earthquakes", title = "Earthquakes each season")
    fig.show()
graphData()