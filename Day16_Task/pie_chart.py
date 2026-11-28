#8. Pie Chart with Conditional Data 
'''Scenario: 
scores = np.array([40, 60, 80, 30, 90]) 
Task: 
● Categorize into: 
○ Pass (>50) 
○ Fail (<=50) 
● Count using NumPy/Pandas 
● Plot pie chart for Pass vs Fail
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Student scores
scores = np.array([40, 60, 80, 30, 90])

# Step 2: Categorize Pass and Fail
pass_count = np.sum(scores > 50)
fail_count = np.sum(scores <= 50)

# Step 3: Create categories
categories = ["Pass", "Fail"]

# Step 4: Store counts
counts = [pass_count, fail_count]

# Step 5: Print results
print("Pass Students:", pass_count)
print("Fail Students:", fail_count)

# Step 6: Create DataFrame
df = pd.DataFrame({
    "Category": categories,
    "Count": counts
})

print("\nPass and Fail Data:")
print(df)

# Step 7: Create pie chart
plt.pie(
    counts,
    labels=categories,
    autopct="%1.1f%%",
    startangle=90
)

# Step 8: Add title
plt.title("Pass vs Fail Student Distribution")

# Step 9: Display chart
plt.show()
