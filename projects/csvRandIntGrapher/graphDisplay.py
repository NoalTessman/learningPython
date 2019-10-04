import plotly.express as px
import pandas as pd
df = pd.read_csv('./out.csv')
#works first try
fig = px.line(df, x = 'series', y = 'number', title='random numbers')
fig.show()