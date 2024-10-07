import altair as alt
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

# price
line_price = alt.Chart(df).mark_line(point=True).encode(
    x=alt.X('createdat:T', title='Date'),
    y=alt.Y('price:Q', title='Price'),
    tooltip=['createdat:T', 'price:Q']
).properties(
    title='Price History'
)

# sold
line_sold = alt.Chart(df).mark_line(point=True, color='green').encode(
    x=alt.X('createdat:T', title='Date'),
    y=alt.Y('sold:Q', title='Sold Items'),
    tooltip=['createdat:T', 'sold:Q']
).properties(
    title='Sold Items Over Time'
)

# Combine charts
combined_chart = alt.layer(line_price, line_sold).resolve_scale(
    y='independent'  # Keep separate y-axes for 'price' and 'sold'
)

# print
combined_chart.save('Graphs\Altair\Altair_line_graph.html')
combined_chart.show('Graphs\Altair\Altair_line_graph.html')     