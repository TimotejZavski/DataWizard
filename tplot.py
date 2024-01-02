
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_json('/Users/timzav/Desktop/test/test/wwwroot/uploads/airbnb.json')

# Scatter plot: price vs number_of_reviews
fig_price_reviews = px.scatter(df, x='price', y='number_of_reviews', color='neighbourhood_group')
fig_price_reviews.write_image('/Users/timzav/Desktop/test/test/wwwroot/images/price_vs_reviews.png')

# Scatter plot: latitude and longitude
fig_geo_dist = px.scatter(df, x='longitude', y='latitude', size='availability_365', color='neighbourhood_group')
fig_geo_dist.write_image('/Users/timzav/Desktop/test/test/wwwroot/images/geographic_distribution.png')

# Bar chart: neighbourhood_groups by average reviews_per_month
grouped_neighbourhood = df.groupby('neighbourhood_group')['reviews_per_month'].agg(['mean', 'std'])
plt.figure(figsize=(10, 8))
sns.barplot(x='mean', y=grouped_neighbourhood.index, xerr=grouped_neighbourhood['std'], orient='h', data=grouped_neighbourhood)
plt.xlabel('Average Reviews per Month')
plt.ylabel('Neighbourhood Group')
plt.title('Neighbourhood Groups by Average Reviews per Month')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/images/avg_reviews_per_month.png')
