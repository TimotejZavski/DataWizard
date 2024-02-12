
import json
import matplotlib.pyplot as plt
from collections import defaultdict

# Load the data from the JSON file
file_path = '/Users/timzav/Desktop/datasets/data/new_york/use_me.json'

# Read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# Create a dictionary for type and prices
type_prices = defaultdict(list)

# Populate the dictionary with type and prices
for item in data:
    type_prices[item['TYPE']].append(int(item['PRICE']))

# Calculate average price per type
average_prices = {house_type: sum(prices) / len(prices) for house_type, prices in type_prices.items()}

# Data for plotting
types = list(average_prices.keys())
avg_prices = list(average_prices.values())

# Plot
plt.figure(figsize=(19.20, 10.80))
plt.bar(types, avg_prices, color='lightblue')

plt.xlabel('Type of House')
plt.ylabel('Average Price ($)')
plt.title('Average Price per Type of House')
plt.xticks(rotation=45, ha='right')

# Save the plot as a PNG image
output_file_path = '/Users/timzav/Desktop/zacasno/average_price_per_type.png'
plt.savefig(output_file_path, format='png', dpi=100)
plt.close()
