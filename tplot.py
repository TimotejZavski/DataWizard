
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Read data from JSON file
data_path = '/Users/timzav/Desktop/DataWizard/test/wwwroot/uploads/Indian Liver Patient Dataset (ILPD).json'
data = pd.read_json(data_path)

# Ensure the output directory exists
output_dir_path = '/Users/timzav/Desktop/DataWizard/test/wwwroot/images/'
Path(output_dir_path).mkdir(parents=True, exist_ok=True)

# Set plot aesthetics
sns.set(style="whitegrid", palette=sns.color_palette("Blues_r"))
plt.rcParams.update({'figure.autolayout': True, 'figure.figsize': (8, 6), 'figure.dpi': 300})

# Helper function to save plots
def save_figure(figure, title):
    filename = title.replace(" ", "_")
    figure.savefig(f"{output_dir_path}{filename}.png", bbox_inches='tight', dpi=300)

# Scatter plot of Alkphos vs Sgpt
plt.figure()
alkphos_sgpt_scatter = sns.scatterplot(x='Alkphos', y='Sgpt', data=data)
alkphos_sgpt_scatter.set_title('Alkphos vs Sgpt')
save_figure(alkphos_sgpt_scatter.get_figure(), 'Alkphos_vs_Sgpt')
plt.close()

# Boxplot of Alkphos by Gender
plt.figure()
alkphos_gender_boxplot = sns.boxplot(x='Gender', y='Alkphos', data=data)
alkphos_gender_boxplot.set_title('Alkphos by Gender')
save_figure(alkphos_gender_boxplot.get_figure(), 'Alkphos_by_Gender')
plt.close()

# Distribution of Sgpt
plt.figure()
sgpt_distplot = sns.histplot(data['Sgpt'], kde=True)
sgpt_distplot.set_title('Distribution of Sgpt')
save_figure(sgpt_distplot.get_figure(), 'Distribution_of_Sgpt')
plt.close()

# Line plot of Total Proteins by Age
plt.figure()
tp_age_lineplot = sns.lineplot(x='Age', y='TP', data=data, ci=None)
tp_age_lineplot.set_title('Total Proteins by Age')
save_figure(tp_age_lineplot.get_figure(), 'Total_Proteins_by_Age')
plt.close()

# Scatter plot of Alkphos vs ALB
plt.figure()
alkphos_alb_scatter = sns.scatterplot(x='Alkphos', y='ALB', data=data)
alkphos_alb_scatter.set_title('Alkphos vs ALB')
save_figure(alkphos_alb_scatter.get_figure(), 'Alkphos_vs_ALB')
plt.close()
