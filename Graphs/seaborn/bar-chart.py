import seaborn as sns
import matplotlib.pyplot as plt
import json

# JSON data
data = '{"values": [10, 20, 15, 25, 30], "labels": ["A", "B", "C", "D", "E"]}'
json_data = json.loads(data)

# bar plot
sns.barplot(x=json_data['labels'], y=json_data['values'])
plt.title('Seaborn Bar Plot Example')
plt.show()