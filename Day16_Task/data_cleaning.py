#10. Data Cleaning + Visualization 
'''Scenario: 
data = np.array([100, np.nan, 200, 150, np.nan, 300]) 
Task: 
1. Convert to Pandas Series 
2. Replace NaN with mean 
3. Plot: 
○ Line graph of cleaned data 
○ Bar chart of values > average
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create data with missing values
data = np.array([100, np.nan, 200, 150, np.nan, 300])

# Step 2: Convert into Pandas Series
series = pd.Series(data)

print("Original Data:")
print(series)

# Step 3: Calculate mean
mean_value = series.mean()

print("\nMean Value:", mean_value)

# Step 4: Replace NaN with mean
cleaned_data = series.fillna(mean_value)

print("\nCleaned Data:")
print(cleaned_data)

# Step 5: Create line graph
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(cleaned_data, marker="o")
plt.title("Line Graph of Cleaned Data")
plt.xlabel("Index")
plt.ylabel("Values")
plt.grid(True)

# Step 6: Filter values greater than average
filtered_data = cleaned_data[cleaned_data > mean_value]

print("\nValues Greater Than Average:")
print(filtered_data)

# Step 7: Create bar chart
plt.subplot(1, 2, 2)
plt.bar(filtered_data.index, filtered_data.values)
plt.title("Values Greater Than Average")
plt.xlabel("Index")
plt.ylabel("Values")

# Step 8: Adjust layout
plt.tight_layout()

# Step 9: Display graphs
plt.show()
