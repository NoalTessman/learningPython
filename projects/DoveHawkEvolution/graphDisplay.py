import plotly.express as px
import pandas as pd
df = pd.read_csv('./25 Birds 25Octagons 2 food Doves Only.csv')
#works first try
fig = px.line(df, x = 'bird Amount', y = 'Generation', title='25 birds 50 octagons')
fig.show()