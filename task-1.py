import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_url = r"C:\Users\shrey\OneDrive\Desktop\Task-01\dataset\API_SP.POP.TOTL_DS2_en_csv_v2_85.csv"
df = pd.read_csv(data_url, skiprows=4)

# For the purpose of this example, let's say we're interested in visualizing the population distribution by country.
# You can replace 'Country Name' with any categorical variable of interest.

# Filter out missing values
df = df.dropna(subset=['Country Name', '2020'])

# Sort the data by population in descending order
df.sort_values(by='2020', ascending=False, inplace=True)

# Select top 10 countries by population
top_10 = df.head(10)

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_10['Country Name'], top_10['2020'] / 1e9, color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population (Billions)')
plt.title('Top 10 Countries by Population in 2020')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
