#3. Employee Salary Insights 
'''Scenario: 
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000]) 
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"] 
Task: 
● Convert into DataFrame 
● Plot: 
○ Line graph → salary trend 
○ Bar chart → department-wise salary comparison 
○ Pie chart → department distribution 
○ Histogram → salary distribution 
○ Scatter plot → index vs salary
'''
# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create salary data using NumPy array
salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])

# Create list of departments
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

# Convert data into DataFrame
df = pd.DataFrame({
    "Department": departments,
    "Salary": salaries
})

# Display the DataFrame
print("Employee Salary Data:")
print(df)

# 1. Line Graph - Shows salary trend
plt.figure(figsize=(7, 4))
plt.plot(salaries, marker='o')
plt.title("Employee Salary Trend")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.grid(True)
plt.show()

# 2. Bar Chart - Department-wise salary comparison
dept_salary = df.groupby("Department")["Salary"].mean()

plt.figure(figsize=(7, 4))
plt.bar(dept_salary.index, dept_salary.values, color='skyblue')
plt.title("Department-wise Salary Comparison")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# 3. Pie Chart - Shows department distribution
dept_count = df["Department"].value_counts()

plt.figure(figsize=(7, 4))
plt.pie(dept_count, labels=dept_count.index, autopct='%1.1f%%')
plt.title("Department Distribution")
plt.show()

# 4. Histogram - Shows salary distribution
plt.figure(figsize=(7, 4))
plt.hist(salaries, bins=5, edgecolor='black')
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# 5. Scatter Plot - Shows index vs salary
plt.figure(figsize=(7, 4))
plt.scatter(range(1, 7), salaries, color='red')
plt.title("Employee Index vs Salary")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()
