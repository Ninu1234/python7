import pandas as pd
import plotly.figure_factory as ff 
import csv
df = pd.read_csv('normal-distribution.csv')
height = df['Height(Inches)'].tolist()
fig = ff.create_distplot([height],['height'],show_hist =False)
fig.show()