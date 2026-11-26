#3. Accessing Specific Data (Indexing) 
'''A Series contains: 
S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"]) 
Task: 
● Access values for B and D 
● Return them as a subset
'''
import pandas as pd

S = pd.Series([100, 200, 300, 400], index=["A", "B", "C", "D"])

# Access values for B and D
print("Value of B:", S["B"])
print("Value of D:", S["D"])

# Return them as subset
result = S[["B", "D"]]

print("Subset:")
print(result)
