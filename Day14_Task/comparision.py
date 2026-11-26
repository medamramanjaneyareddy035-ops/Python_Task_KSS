#1. Fruit Sales Comparison (Series Addition) 
'''A shop tracks fruit sales: 
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"]) 
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"]) 
Task: 
● Add both series 
● Find the total sales of all fruits combined
'''
import pandas as pd

S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"]) 
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])

# Add both series
result = S1 + S2

print("Fruits Sales:")
print(result)

#Total sales
print("Total sales:", result.sum())

