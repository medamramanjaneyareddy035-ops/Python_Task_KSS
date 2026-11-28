#2. Student Marks Bar Chart 
'''Scenario: 
Marks of students: 
names = ["A", "B", "C", "D"] 
marks = np.array([70, 85, 60, 90]) 
Task: 
● Create a DataFrame 
● Plot a bar graph 
● Show student names on X-axis
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"] 
marks = np.array([70, 85, 60, 90])

# Create Data Frame

df = pd.DataFrame({"Names" : names, "Marks" : marks })

print(df)

# Plot bar graph
plt.bar(df["Marks"], df["Names"])

plt.xlabel("Students Names")
plt.ylabel("Marka")
plt.title("Students Marks Bar chart")

plt.show()
