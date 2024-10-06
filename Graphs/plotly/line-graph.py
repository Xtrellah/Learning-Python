import plotly.graph_objs as go
import json
from datetime import datetime

# data
with open('Graphs/data.json', 'r') as file:
    data = json.load(file)
history = data['history']

# graph stuff
dates = [datetime.strptime(item['createdat'], "%Y-%m-%dT%H:%M:%S%z").date() for item in history]
prices = [item['price'] for item in history]
sold = [item['sold'] for item in history]

trace_price = go.Scatter(x=dates, y=prices, mode='lines+markers', name='Price')
trace_sold = go.Scatter(x=dates, y=sold, mode='lines+markers', name='Sold Items')

layout = go.Layout(
    title="Item Price History",
    xaxis_title="Date",
    yaxis_title="Values",
    hovermode="closest"
)

fig = go.Figure(data=[trace_price, trace_sold], layout=layout)

fig.show()
