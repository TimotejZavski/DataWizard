
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
candy_data = pd.read_json('/Users/timzav/Desktop/test/test/wwwroot/uploads/candy.json')

# Chart 1: Bar plot of win percentage by chocolate presence
chocolate_win = candy_data.groupby('chocolate')['winpercent'].mean().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='chocolate', y='winpercent', data=chocolate_win)
plt.title('Win Percentage by Chocolate Presence')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/images/chocolate_win_percent.png')
plt.close()

# Chart 2: Histogram of sugar percentage
plt.figure(figsize=(10, 6))
sns.histplot(candy_data['sugarpercent'], kde=True, bins=10)
plt.title('Sugar Percentage Distribution')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/images/sugar_percent_distribution.png')
plt.close()

# Chart 3: Scatter plot of win percent vs. price percent
plt.figure(figsize=(10, 6))
sns.scatterplot(x='pricepercent', y='winpercent', hue='chocolate', data=candy_data)
plt.title('Win Percent vs. Price Percent')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/images/win_vs_price.png')
plt.close()

# Chart 4: Box plot of win percent by bar type
plt.figure(figsize=(10, 6))
sns.boxplot(x='bar', y='winpercent', data=candy_data)
plt.title('Win Percent by Bar Type')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/images/win_percent_by_bar.png')
plt.close()

# Chart 5: Pie chart of candy types with and without peanuts or almonds
peanuts_almonds_counts = candy_data['peanutyalmondy'].value_counts()
fig = px.pie(values=peanuts_almonds_counts, names=peanuts_almonds_counts.index, title='Candy Types with and without Peanuts/Almonds')
fig.write_image('/Users/timzav/Desktop/test/test/wwwroot/images/peanuts_almonds_pie_chart.png')
