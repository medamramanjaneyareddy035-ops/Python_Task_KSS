#8. Complex DataFrame Transformation 
'''A DataFrame: 
df = pd.DataFrame({ 
"Name": ["A", "B", "C", "D"], 
"Marks": [50, 80, 30, 90] 
}) 
Scenario: 
● Students scoring below 50 failed 
Task: 
1. Create a column Status ("Pass"/"Fail") 
2. Filter only passed students 
3. Calculate average marks of passed students
'''
import pandas as pd
df = pd.DataFrame({ 
"Name": ["A", "B", "C", "D"], 
"Marks": [50, 80, 30, 90] 
})

# Create Status column
df["Status"] = df["Marks"].apply(lambda x: "pass" if x >= 50 else "Fail")

print("Complete DataFrame:")
print(df)

# filter passed students
passed = df[df["Status"] == "pass"]

print("\n passed students:")
print(passed)

# Calculate average marks
average = passed["Marks"].mean()

print("\n Average Marks:", average)
