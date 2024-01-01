
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_json('/Users/timzav/Desktop/test/test/wwwroot/uploads/train.json')

# Sort the dataframe by duration_ms
sorted_df = df.sort_values(by='duration_ms', ascending=True)

# Plot the sorted dataframe
plt.figure(figsize=(10, 8))
plt.barh(sorted_df['track_name'][:10], sorted_df['duration_ms'][:10])  # Only display top 10
plt.xlabel('Duration in ms')
plt.ylabel('Track Name')
plt.title('Top 10 Tracks Sorted by Duration')
plt.tight_layout()

# Save the figure
plt.savefig('/Users/timzav/Desktop/test/test/wwwroot/p_images/sorted_tracks_duration.png')
