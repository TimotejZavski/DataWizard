
import json
import matplotlib.pyplot as plt

# Load data from the JSON file
with open('/Users/timzav/Desktop/datasets/data/new_york/use_me.json') as json_file:
    data = json.load(json_file)

# Extract relevant data
prices = [int(item["PRICE"]) for item in data if item["PRICE"].isdigit()]
properties = [item["MAIN_ADDRESS"] for item in data]

# Generate a bar chart
plt.figure(figsize=(1920/96, 1080/96), dpi=96)
plt.bar(properties, prices, color='lightblue')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=90, ha='right', fontsize=8)

# Set chart title and labels
plt.title('Property Prices in New York', fontsize=18)
plt.xlabel('Property', fontsize=14)
plt.ylabel('Price ($)', fontsize=14)

# Save the chart as a high-resolution PNG image
plt.tight_layout()
plt.savefig('/Users/timzav/Desktop/zacasno/new_york_property_prices.png', format='png', dpi=300)

plt.show()
