#1. Student Score Processor 
'''Scenario: 
A teacher stores student names and marks in a list of tuples. 
Task: 
● Convert data into a dictionary 
● Use a loop + condition to find students scoring above 50 
● Use math module to calculate average 
● Store results in a text file
'''
import math

# List of tuples
students = [
    ("Ram", 80),
    ("Ravi", 45),
    ("Krishna", 90),
    ("Arjun", 60),
    ("Sai", 30)
]

# Convert into dictionary
student_dict = dict(students)

print("Student Dictionary:")
print(student_dict)

# Find students scoring above 50
passed = []

for name, marks in student_dict.items():
    if marks > 50:
        passed.append((name, marks))

print("\nStudents scoring above 50:")
print(passed)

# Calculate average using math module
total = sum(marks for name, marks in passed)
average = math.floor(total / len(passed))

print("\nAverage Marks:", average)

# Store results in text file
with open("student_results.txt", "w") as file:
    file.write("Student Results\n")
    file.write(str(student_dict) + "\n")
    file.write("Students above 50:\n")
    file.write(str(passed) + "\n")
    file.write("Average Marks: " + str(average))

print("\nResults saved successfully!")
