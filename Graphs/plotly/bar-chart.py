import plotly.express as px
import json

# data
data = '{"values": [1, 2, 3, 4, 5], "labels": ["A", "B", "C", "D", "E"]}'
json_data = json.loads(data)

# bar chart
fig = px.bar(x=json_data['labels'], y=json_data['values'], title="Plotly Bar Chart Example")
fig.show()
