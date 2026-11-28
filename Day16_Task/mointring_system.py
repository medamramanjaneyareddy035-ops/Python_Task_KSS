#4. Temperature Monitoring System 
'''Scenario: 
temps = np.array([28, 30, 32, 35, 33, 31, 29]) 
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → daily temperature trend 
○ Bar chart → day-wise temperature 
○ Pie chart → proportion of high (>30) vs low temps 
○ Histogram → temperature frequency 
○ Scatter plot → day index vs temperature
'''
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create temperature data using NumPy array
temps = np.array([28, 30, 32, 35, 33, 31, 29])

# Create list of days
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Create DataFrame using Pandas
df = pd.DataFrame({
    "Day": days,
    "Temperature": temps
})

# Display the DataFrame
print("Weekly Temperature Data:")
print(df)

# 1. Line Graph - Shows daily temperature trend
plt.figure(figsize=(7, 4))
plt.plot(days, temps, marker='o')
plt.title("Daily Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# 2. Bar Chart - Shows day-wise temperature
plt.figure(figsize=(7, 4))
plt.bar(days, temps, color='skyblue')
plt.title("Day-wise Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.show()

# 3. Pie Chart - Shows proportion of high and low temperatures
high = np.sum(temps > 30)
low = np.sum(temps <= 30)

plt.figure(figsize=(7, 4))
plt.pie([high, low], labels=["High (>30)", "Low (<=30)"],
        autopct='%1.1f%%')
plt.title("High vs Low Temperature")
plt.show()

# 4. Histogram - Shows temperature frequency
plt.figure(figsize=(7, 4))
plt.hist(temps, bins=5, edgecolor='black')
plt.title("Temperature Frequency")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot - Shows day index vs temperature
plt.figure(figsize=(7, 4))
plt.scatter(range(1, 8), temps, color='red')
plt.title("Day Index vs Temperature")
plt.xlabel("Day Index")
plt.ylabel("Temperature (°C)")
plt.show()
