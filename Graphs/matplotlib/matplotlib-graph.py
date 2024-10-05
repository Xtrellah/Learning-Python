import matplotlib.pyplot as plt
import json

# JSON
data = '{"values": [1, 2, 3, 4, 5], "labels": ["A", "B", "C", "D", "E"]}'
json_data = json.loads(data)

# Bar chart
plt.bar(json_data['labels'], json_data['values'])
plt.xlabel('Labels')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()
