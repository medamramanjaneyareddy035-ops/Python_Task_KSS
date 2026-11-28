#9. Combined Visualization Dashboard 
'''Scenario: 
sales = np.array([100, 200, 150, 300]) 
products = ["A", "B", "C", "D"] 
Task: 
● Create DataFrame 
● Plot: 
○ Line graph (trend) 
○ Bar chart (comparison) 
○ Pie chart (distribution) 
● Show all in single figure (subplots)
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create sales data
sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

# Step 2: Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print("Product Sales Data:")
print(df)

# Step 3: Create a single figure with 3 subplots
plt.figure(figsize=(15, 5))

# Graph 1: Line graph
plt.subplot(1, 3, 1)
plt.plot(df["Product"], df["Sales"], marker="o")
plt.title("Sales Trend")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.grid(True)

# Graph 2: Bar chart
plt.subplot(1, 3, 2)
plt.bar(df["Product"], df["Sales"])
plt.title("Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

# Graph 3: Pie chart
plt.subplot(1, 3, 3)
plt.pie(
    df["Sales"],
    labels=df["Product"],
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Sales Distribution")

# Step 4: Adjust layout
plt.tight_layout()

# Step 5: Display all graphs
plt.show()
