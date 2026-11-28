#4. Temperature Trend Line Plot 
'''Scenario: 
Daily temperatures: 
temps = np.array([28, 30, 32, 31, 29]) 
Task: 
● Convert into Pandas Series 
● Plot a line graph 
● Add title and grid
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Daily temperatures
temps = np.array([28, 30, 32, 31, 29])

# Step 2: Convert into Pandas Series
temperature_series = pd.Series(temps)

print("Temperature Data:")
print(temperature_series)

# Step 3: Plot line graph
plt.plot(temperature_series, marker='o')

# Step 4: Add title and labels
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")

# Step 5: Add grid
plt.grid(True)

# Step 6: Display graph
plt.show()
