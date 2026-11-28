#2. Monthly Sales Analysis 
'''Scenario: 
sales = np.array([100, 150, 200, 180, 220, 300]) 
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → month-wise comparison 
○ Pie chart → contribution of each month 
○ Histogram → frequency of sales values 
○ Scatter plot → month index vs sales
'''
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sales data using NumPy array
sales = np.array([100, 150, 200, 180, 220, 300])

# Create list of months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

# Create a DataFrame using Pandas
df = pd.DataFrame({
    "Month": months,
    "Sales": sales
})

# Display the DataFrame
print("Monthly Sales Data:")
print(df)

# 1. Line Graph - Shows the sales trend
plt.figure(figsize=(7, 4))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Bar Chart - Compares sales of each month
plt.figure(figsize=(7, 4))
plt.bar(months, sales, color='skyblue')
plt.title("Month-wise Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# 3. Pie Chart - Shows contribution of each month
plt.figure(figsize=(7, 4))
plt.pie(sales, labels=months, autopct='%1.1f%%')
plt.title("Monthly Sales Contribution")
plt.show()

# 4. Histogram - Shows frequency of sales values
plt.figure(figsize=(7, 4))
plt.hist(sales, bins=5, edgecolor='black')
plt.title("Frequency of Sales Values")
plt.xlabel("Sales Values")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot - Shows month index vs sales
plt.figure(figsize=(7, 4))
plt.scatter(range(1, 7), sales, color='red')
plt.title("Month Index vs Sales")
plt.xlabel("Month Index")
plt.ylabel("Sales")
plt.show()
