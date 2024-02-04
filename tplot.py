
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# Load the JSON data
file_path = '/Users/timzav/Desktop/DataWizard/test/wwwroot/uploads/Indian Liver Patient Dataset (ILPD) 2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Analyze the structure of the data
# Gender distribution
gender_counts = df['Gender'].value_counts()

# Age distribution
age_distribution = df['Age'].value_counts().sort_index()

# Liver disease by age
liver_disease_age = df.groupby('Age')['Selector'].mean()

# Use the specified color palette for the charts
color_palette = sns.color_palette("Blues")

# Create the specified charts based on the analysis

# Chart 1: Gender distribution
plt.figure(figsize=(8, 6), dpi=1920/8)
sns.countplot(x='Gender', data=df, palette=color_palette)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Gender')
plt.savefig('/Users/timzav/Desktop/DataWizard/test/wwwroot/images/gender_distribution.png', bbox_inches='tight')

# Chart 2: Age distribution
plt.figure(figsize=(8, 6), dpi=1920/8)
age_distribution.plot(kind='bar', color=color_palette)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Age Distribution')
plt.savefig('/Users/timzav/Desktop/DataWizard/test/wwwroot/images/age_distribution.png', bbox_inches='tight')

# Chart 3: Liver disease by age
plt.figure(figsize=(8, 6), dpi=1920/8)
liver_disease_age.plot(kind='line', color=color_palette[2])
plt.title('Liver Disease by Age')
plt.xlabel('Age')
plt.ylabel('Average Selector Value')
plt.legend(title='Liver Disease')
plt.savefig('/Users/timzav/Desktop/DataWizard/test/wwwroot/images/liver_disease_by_age.png', bbox_inches='tight')

# Delete the charts' figures to clear memory
plt.close('all')
