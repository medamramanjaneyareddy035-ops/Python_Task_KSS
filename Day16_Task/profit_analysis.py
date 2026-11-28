#5. Product Sales & Profit Analysis 
'''Scenario: 
sales = np.array([200, 300, 250, 400, 350]) 
profit = np.array([50, 70, 60, 90, 80]) 
products = ["A", "B", "C", "D", "E"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph → sales trend 
○ Bar chart → product vs sales 
○ Pie chart → sales contribution 
○ Histogram → profit distribution 
○ Scatter plot → sales vs profit
'''
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create sales data using NumPy array
sales = np.array([200, 300, 250, 400, 350])

# Create profit data using NumPy array
profit = np.array([50, 70, 60, 90, 80])

# Create list of products
products = ["A", "B", "C", "D", "E"]

# Create DataFrame using Pandas
df = pd.DataFrame({
    "Product": products,
    "Sales": sales,
    "Profit": profit
})

# Display the DataFrame
print("Product Sales and Profit Data:")
print(df)

# 1. Line Graph - Shows sales trend
plt.figure(figsize=(7, 4))
plt.plot(products, sales, marker='o')
plt.title("Product Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# 2. Bar Chart - Compares product sales
plt.figure(figsize=(7, 4))
plt.bar(products, sales, color='skyblue')
plt.title("Product-wise Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# 3. Pie Chart - Shows sales contribution
plt.figure(figsize=(7, 4))
plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title("Product Sales Contribution")
plt.show()

# 4. Histogram - Shows profit distribution
plt.figure(figsize=(7, 4))
plt.hist(profit, bins=5, edgecolor='black')
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot - Shows sales vs profit
plt.figure(figsize=(7, 4))
plt.scatter(sales, profit, color='red')
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()
