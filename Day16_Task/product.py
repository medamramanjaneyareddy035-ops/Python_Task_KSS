#5. Product Sales Bar Chart 
'''Scenario: 
products = ["Pen", "Book", "Pencil"] 
sales = np.array([50, 80, 40]) 
Task: 
● Create DataFrame 
● Plot bar chart 
● Add labels and title
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Product names
products = ["Pen", "Book", "Pencil"]

# Step 2: Sales data
sales = np.array([50, 80, 40])

# Step 3: Create DataFrame
df = pd.DataFrame({
    "Product": products,
    "Sales": sales
})

print("Product Sales Data:")
print(df)

# Step 4: Create bar chart
plt.bar(df["Product"], df["Sales"])

# Step 5: Add title and labels
plt.title("Product Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Sales Quantity")

# Step 6: Display graph
plt.show()
