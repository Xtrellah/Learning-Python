import json
import matplotlib.pyplot as plt
from datetime import datetime

# json shi
with open('Graphs/data.json', 'r') as file:
    data = json.load(file)

history = data['history']

dates = [datetime.strptime(item['createdat'], "%Y-%m-%dT%H:%M:%S%z") for item in history]
prices = [item['price'] for item in history]
sold = [item['sold'] for item in history]

# plot size
plt.figure(figsize=(12, 6))

# styling
plt.plot(dates, prices, label='Price', color='blue', marker='o')
plt.plot(dates, sold, label='Sold', color='green', marker='o')

plt.title('Price and Sold History Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.legend() 
plt.grid(True)

plt.tight_layout()
plt.show()
