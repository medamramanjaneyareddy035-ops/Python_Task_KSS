#6. Multi-Line Graph for Sales Comparison 
'''Scenario: 
data = { 
"Month": ["Jan", "Feb", "Mar"], 
"Store_A": [100, 150, 200], 
"Store_B": [90, 140, 210] 
} 
Task: 
● Create DataFrame 
● Plot two line graphs on same plot 
● Add legend
'''
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create sales data
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Store_A": [100, 150, 200],
    "Store_B": [90, 140, 210]
}

# Step 2: Create DataFrame
df = pd.DataFrame(data)

print("Sales Data:")
print(df)

# Step 3: Plot Store A sales
plt.plot(
    df["Month"],
    df["Store_A"],
    marker="o",
    label="Store A"
)

# Step 4: Plot Store B sales
plt.plot(
    df["Month"],
    df["Store_B"],
    marker="s",
    label="Store B"
)

# Step 5: Add title and labels
plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales")

# Step 6: Add legend
plt.legend()

# Step 7: Add grid
plt.grid(True)

# Step 8: Display graph
plt.show()
