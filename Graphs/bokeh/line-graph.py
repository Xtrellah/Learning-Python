from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import HoverTool
import pandas as pd
import json
from datetime import datetime

# data
with open('Graphs/data.json', 'r') as f:
    data = json.load(f)

history = data['history']

# convert to pandas DataFrame
df = pd.DataFrame(history)

# createdat to datetime
df['createdat'] = pd.to_datetime(df['createdat'])

# output file
output_file('Graphs\Bokeh\Bokeh_graph.html')

# plot
p = figure(title="Item History",
           x_axis_label='Date', y_axis_label='Values',
           x_axis_type='datetime')

# price
p.line(df['createdat'], df['price'], legend_label='Price', line_width=2, color='blue')
p.circle(df['createdat'], df['price'], size=8, color='blue', legend_label='Price')

# sold
p.line(df['createdat'], df['sold'], legend_label='Sold Items', line_width=2, color='green')
p.circle(df['createdat'], df['sold'], size=8, color='green', legend_label='Sold Items')

# hover info
hover = HoverTool()
hover.tooltips = [
    ('Date', '@x{%F}'),
    ('Price', '@y'),
]
hover.formatters = {'@x': 'datetime'}
p.add_tools(hover)

# print
show(p)