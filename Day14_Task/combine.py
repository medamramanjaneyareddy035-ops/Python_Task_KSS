#8. Combine NumPy Arrays into DataFrame 
'''Two arrays: 
names = np.array(["A", "B", "C"]) 
marks = np.array([80, 90, 70]) 
Task: 
● Create a DataFrame with columns "Name" and "Marks" 
● Filter students with marks above 75
'''
import numpy as np
import pandas as pd

names = np.array(["A", "B", "C"]) 
marks = np.array([80, 90, 70])

d = pd.DataFrame({
    "Name": names,
    "Marks":marks
    })
print("Complete DataFrame:")
print(d)

print("\nStudents with marks above 75:")
print(d[d["Marks"] > 75])
