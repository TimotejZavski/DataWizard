
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data from the JSON file
data_path = '/Users/timzav/Desktop/test/test/wwwroot/uploads/penguins.json'
df = pd.read_json(data_path)

# Create plots directory if it does not exist
images_dir = '/Users/timzav/Desktop/test/test/wwwroot/images/'
if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Example plots

# Histogram of culmen length
plt.figure(figsize=(8, 6))
sns.histplot(df['culmen_length_mm'])
plt.title('Histogram of Culmen Length')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Count')
culmen_length_hist_path = os.path.join(images_dir, 'culmen_length_hist.png')
plt.savefig(culmen_length_hist_path)
plt.close()

# Scatter plot of culmen depth vs flipper length
plt.figure(figsize=(8, 6))
sns.scatterplot(x='culmen_depth_mm', y='flipper_length_mm', hue='sex', data=df)
plt.title('Culmen Depth vs. Flipper Length by Sex')
plt.xlabel('Culmen Depth (mm)')
plt.ylabel('Flipper Length (mm)')
culmen_depth_flipper_scatter_path = os.path.join(images_dir, 'culmen_depth_flipper_scatter.png')
plt.savefig(culmen_depth_flipper_scatter_path)
plt.close()

# Pairplot
sns.pairplot(df, hue='sex')
pairplot_path = os.path.join(images_dir, 'pairplot.png')
plt.savefig(pairplot_path)
plt.close()
