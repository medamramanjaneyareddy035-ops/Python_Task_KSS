#7. Data Alignment Issue in Series Addition 
'''Two Series: 
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) 
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"]) 
Task: 
● Add both Series 
● Explain why some values become NaN 
● Replace NaN with 0 and compute final result
'''
import pandas as pd

S1 = pd.Series([10, 20, 30], index=["a", "b", "c"]) 
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])

# add both series
result = S1 + S2
print("Addtion:")
print(result)

# replace NaN with 0
final_result = result.fillna(0)

print("Final result:")
print(final_result)
