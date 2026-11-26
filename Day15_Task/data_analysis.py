#6. Data Analysis Tool (NumPy + Pandas) 
'''Scenario: 
Analyze student marks. 
Task: 
● Generate marks using NumPy 
● Convert into Pandas DataFrame 
● Use conditions to filter passing students 
● Calculate mean using math/NumPy 
● Use loop to print results
'''
import numpy as np
import pandas as pd

# Generate student marks using NumPy
marks = np.array([85, 45, 90, 35, 75, 60, 95, 25])

# Student names
names = ["Ram", "Ravi", "Sita", "Raju",
         "Kiran", "Arun", "Priya", "John"]

# Convert into Pandas DataFrame
data = {
    "Name": names,
    "Marks": marks
}

df = pd.DataFrame(data)

print("Student Marks:")
print(df)

# Filter passing students
passing = df[df["Marks"] >= 40]

print("\nPassing Students:")
print(passing)

# Calculate mean
mean_marks = np.mean(marks)

print("\nAverage Marks:", mean_marks)

# Display results using loop
print("\nStudent Results:")

for index, row in df.iterrows():
    if row["Marks"] >= 40:
        print(row["Name"], "- Pass")
    else:
        print(row["Name"], "- Fail")
