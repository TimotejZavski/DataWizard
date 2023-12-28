
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Read the data
df = pd.read_json('/Users/timzav/Desktop/test/test/wwwroot/uploads/penguins.json')

# Clean the data
df.dropna(inplace=True)
df['sex'] = df['sex'].str.strip()

# Create a pairplot
sns.pairplot(df, hue='sex', diag_kind='kde')
plt.savefig('pairplot.png')

# Create a scatter plot for culmen_length_mm vs culmen_depth_mm
plt.figure()
sns.scatterplot(data=df, x='culmen_length_mm', y='culmen_depth_mm', hue='sex')
plt.savefig('scatter_culmen.png')

# Create a histogram for flipper_length_mm
plt.figure()
sns.histplot(df, x='flipper_length_mm', hue='sex', kde=True)
plt.savefig('hist_flipper.png')

# Create a boxplot for body_mass_g
plt.figure()
sns.boxplot(data=df, x='sex', y='body_mass_g')
plt.savefig('boxplot_body_mass.png')

# Create a violin plot for body mass vs sex using plotly
fig = px.violin(df, y='body_mass_g', color='sex', box=True)
fig.write_image('violin_body_mass_plotly.png')

