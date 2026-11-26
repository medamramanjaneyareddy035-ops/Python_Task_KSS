#10. Row Filtering + Aggregation 
'''A dataset: 
arr = np.array([ 
[100, 200], 
[150, 250], 
[80, 120], 
[300, 400] 
]) 
Task: 
● Convert to DataFrame with columns "Sales", "Profit" 
● Filter rows where Sales > 100 
● Find average Profit of filtered rows
'''
import numpy as np
import pandas as pd

arr = np.array([
    [100, 200],
    [150, 250],
    [80, 120],
    [300, 400]
])

# Convert NumPy array into DataFrame
df = pd.DataFrame(arr, columns=["Sales", "Profit"])

print("Complete DataFrame:")
print(df)

# Filter rows where Sales > 100
filtered = df[df["Sales"] > 100]

print("\nFiltered DataFrame:")
print(filtered)

# Find average Profit of filtered rows
avg_profit = filtered["Profit"].mean()

print("\nAverage Profit:")
print(avg_profit)
