
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

# Load the data
file_path = '/Users/timzav/Desktop/DataWizard/test/wwwroot/uploads/banklist.json'
bank_data = pd.read_json(file_path)

# Convert closing dates to datetime and extract the year
bank_data['Closing Date'] = pd.to_datetime(bank_data['Closing Date'])
bank_data['Year Closed'] = bank_data['Closing Date'].dt.year

# Filter data for years after 2012
bank_data_after_2012 = bank_data[bank_data['Year Closed'] >= 2012]

# Count the number of banks closed each year
bank_closures_per_year = bank_data_after_2012['Year Closed'].value_counts().sort_index()

# Plotting
plt.figure(figsize=(8, 6), dpi=150)
ax = sns.barplot(x=bank_closures_per_year.index.astype(str), y=bank_closures_per_year.values, palette="Blues_d")

# Set chart title and labels
ax.set_title('Bank Closures by Year After 2012', fontsize=14, weight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Number of Bank Closures', fontsize=12)

# Ensure x-axis only has integer ticks for years
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

# Save the figure
output_path = '/Users/timzav/Desktop/DataWizard/test/wwwroot/images/Bank_Closures_by_Year_After_2012.png'
plt.savefig(output_path, bbox_inches='tight', format='png')

# Show plot (not required for saving image)
# plt.show()
