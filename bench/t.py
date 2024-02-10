
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import json
import os

# Load data from the JSON file
file_path = '/Users/timzav/Desktop/datasets/data/new_york/use_me.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert data to DataFrame
df = pd.DataFrame(data)

# Set color palette
sns.set_palette(["#80ced6"])

# Bar Chart for House Types
plt.figure(figsize=(16, 9))
df['TYPE'].value_counts().plot(kind='bar')
plt.title('Distribution of House Types')
plt.xlabel('Type of House')
plt.ylabel('Frequency')
plt.savefig('/Users/timzav/Desktop/zacasno/house_types.png', dpi=300)

# Histogram for Price Distribution
plt.figure(figsize=(16, 9))
sns.histplot(df['PRICE'].astype(float), bins=30)
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.savefig('/Users/timzav/Desktop/zacasno/price_distribution.png', dpi=300)

# Bar Chart for Number of Bedrooms and Bathrooms
fig, axes = plt.subplots(1, 2, figsize=(16, 9))
sns.countplot(ax=axes[0], x='BEDS', data=df)
sns.countplot(ax=axes[1], x='BATH', data=df)
axes[0].set_title('Distribution of Bedrooms')
axes[1].set_title('Distribution of Bathrooms')
plt.savefig('/Users/timzav/Desktop/zacasno/bed_bath_distribution.png', dpi=300)

# Scatter Plot for Price vs. Property Square Footage
plt.figure(figsize=(16, 9))
sns.scatterplot(x='PROPERTYSQFT', y='PRICE', data=df)
plt.title('Price vs Property Square Footage')
plt.xlabel('Property Square Footage')
plt.ylabel('Price')
plt.savefig('/Users/timzav/Desktop/zacasno/price_sqft_scatter.png', dpi=300)

# Map Plotting House Locations
plt.figure(figsize=(16, 9))
sns.scatterplot(x='LONGITUDE', y='LATITUDE', data=df)
plt.title('House Locations in New York')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('/Users/timzav/Desktop/zacasno/house_locations_map.png', dpi=300)
