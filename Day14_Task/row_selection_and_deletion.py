#6. Row Selection & Deletion 
'''A DataFrame: 
df = pd.DataFrame({ 
"A": [10, 20, 30], 
"B": [5, 15, 25] 
}, index=["x", "y", "z"]) 
Task: 
● Select row with index "y" 
● Delete row "x" 
● Print updated DataFrame
'''
import pandas as pd
df = pd.DataFrame({ 
"A": [10, 20, 30], 
"B": [5, 15, 25] 
}, index=["x", "y", "z"])

# select row with index y
selected_row = df.loc["y"]
print("Selected Row('y'): ")

print(selected_row)

# delete row z
df = df.drop("z")

# print updated data frame
print("\n Updated Data Frame:")
print(df)
