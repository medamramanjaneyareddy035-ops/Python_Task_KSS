#7. Filtered Bar Chart 
'''Scenario: 
marks = np.array([45, 80, 60, 30, 90]) 
names = ["A", "B", "C", "D", "E"] 
Task: 
● Convert to DataFrame 
● Filter students with marks > 50 
● Plot bar chart only for filtered students
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Student marks
marks = np.array([45, 80, 60, 30, 90])

# Step 2: Student names
names = ["A", "B", "C", "D", "E"]

# Step 3: Create DataFrame
df = pd.DataFrame({
    "Name": names,
    "Marks": marks
})

print("Original Student Data:")
print(df)

# Step 4: Filter students with marks > 50
filtered_df = df[df["Marks"] > 50]

print("\nFiltered Student Data:")
print(filtered_df)

# Step 5: Plot filtered bar chart
plt.bar(filtered_df["Name"], filtered_df["Marks"])

# Step 6: Add title and labels
plt.title("Students Scoring Above 50")
plt.xlabel("Student Names")
plt.ylabel("Marks")

# Step 7: Add grid
plt.grid(axis="y")

# Step 8: Display chart
plt.show()
