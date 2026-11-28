#1. Student Performance Dashboard 
'''Scenario: 
A school records marks of students in one subject: 
marks = np.array([45, 67, 89, 56, 72, 91, 38]) 
students = ["A", "B", "C", "D", "E", "F", "G"] 
Task: 
● Convert to Pandas DataFrame 
● Plot: 
○ Line graph → trend of marks 
○ Bar chart → student vs marks 
○ Pie chart → Pass (>50) vs Fail 
○ Histogram → distribution of marks 
○ Scatter plot → index vs marks
'''
# =====================================================
# PROJECT: STUDENT PERFORMANCE DASHBOARD
# TOOLS: NUMPY, PANDAS, MATPLOTLIB
# =====================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# SCENARIO 1: DATA CREATION

marks = np.array([45, 67, 89, 56, 72, 91, 38])

students = ["A", "B", "C", "D", "E", "F", "G"]

# SCENARIO 2: CONVERT INTO PANDAS DATAFRAME

df = pd.DataFrame({
    "Student": students,
    "Marks": marks
})

print("\nSTUDENT PERFORMANCE DATA")
print(df)

# SCENARIO 3: BASIC DATA ANALYSIS

print("\nTotal Students:", len(df))
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))

# Pass criteria: Marks greater than 50

df["Result"] = np.where(df["Marks"] > 50, "Pass", "Fail")

print("\nSTUDENT RESULTS")
print(df)

pass_count = np.sum(marks > 50)
fail_count = np.sum(marks <= 50)

print("\nPassed Students:", pass_count)
print("Failed Students:", fail_count)

# SCENARIO 4: LINE GRAPH

plt.figure(figsize=(8, 5))

plt.plot(students, marks, marker='o', color='blue')

plt.title("Student Marks Trend")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)

plt.savefig("line_graph.png")
plt.show()

# SCENARIO 5: BAR CHART

plt.figure(figsize=(8, 5))

plt.bar(students, marks, color='green')

plt.title("Student vs Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.savefig("bar_chart.png")
plt.show()

# SCENARIO 6: PIE CHART

plt.figure(figsize=(7, 7))

plt.pie(
    [pass_count, fail_count],
    labels=["Pass", "Fail"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Pass vs Fail Percentage")

plt.savefig("pie_chart.png")
plt.show()

# SCENARIO 7: HISTOGRAM

plt.figure(figsize=(8, 5))

plt.hist(marks, bins=5, color='orange', edgecolor='black')

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.savefig("histogram.png")
plt.show()

# SCENARIO 8: SCATTER PLOT

plt.figure(figsize=(8, 5))

plt.scatter(range(len(marks)), marks, color='red')

plt.title("Student Index vs Marks")
plt.xlabel("Student Index")
plt.ylabel("Marks")

plt.savefig("scatter_plot.png")
plt.show()

# SCENARIO 9: FINAL SUMMARY

print("\n========== FINAL DASHBOARD ==========")

print("Total Students:", len(df))
print("Average Marks:", round(np.mean(marks), 2))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Pass Count:", pass_count)
print("Fail Count:", fail_count)

print("\nAll Graphs Saved Successfully!")
print("PROJECT COMPLETED!")
