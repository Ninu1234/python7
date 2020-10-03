import pandas as pd
import plotly.figure_factory as ff 
import csv
df = pd.read_csv('normal-distribution.csv')
height = df['Weight(Pounds)'].tolist()
fig = ff.create_distplot([height],['weight'],show_hist =False)
fig.show()