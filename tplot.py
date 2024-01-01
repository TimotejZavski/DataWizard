
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset from JSON file
data_path = '/Users/timzav/Desktop/test/test/wwwroot/uploads/penguins.json'
df = pd.read_json(data_path)

# Plot 1: Scatter plot of culmen_length_mm vs culmen_depth_mm using Plotly
scatter_fig = px.scatter(df, x='culmen_length_mm', y='culmen_depth_mm', color='sex', title='Culmen Length vs Depth')
scatter_fig.write_image('/Users/timzav/Desktop/test/test/wwwroot/p_images/scatter_plot.png')

# Plot 2: Histogram of flipper_length_mm using Matplotlib
plt.figure()
plt.hist(df['flipper_length_mm'].dropna(), bins=20, color='skyblue', edgecolor='black')
plt.title('Flipper Length Distribution')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Frequency')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/p_images/flipper_length_hist.png')
plt.close()

# Plot 3: KDE (Kernel Density Estimate) plot of body_mass_g using Seaborn
plt.figure(figsize=(8, 6))
sns.kdeplot(data=df, x='body_mass_g', shade=True)
plt.title('Body Mass Distribution')
plt.xlabel('Body Mass (g)')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/p_images/body_mass_kde.png')
plt.close()

# Plot 4: Box plot of flipper_length_mm grouped by sex using Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='sex', y='flipper_length_mm')
plt.title('Flipper Length by Sex')
plt.xlabel('Sex')
plt.ylabel('Flipper Length (mm)')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/p_images/flipper_length_boxplot.png')
plt.close()

# Plot 5: Violin plot of body_mass_g grouped by sex using Seaborn
plt.figure(figsize=(8, 6))
sns.violinplot(data=df, x='sex', y='body_mass_g')
plt.title('Body Mass by Sex')
plt.xlabel('Sex')
plt.ylabel('Body Mass (g)')
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/p_images/body_mass_violin.png')
plt.close()
