#10. Advanced Simulation System 
'''Scenario: 
Simulate exam results and generate reports. 
Task: 
● Generate random marks using random 
● Store in NumPy array 
● Convert to Pandas DataFrame 
● Use OOP to represent Student 
● Use conditions + loops to assign grades 
● Save report to file 
● Handle errors using try-except 
● Use math module for statistics
'''
import random
import numpy as np
import pandas as pd
import math


# Student class using OOP
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Assign grade using conditions
    def get_grade(self):

        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"


try:

    # Student names
    names = ["Ram", "Ravi", "Sita", "Raju", "Kiran"]

    # Generate random marks
    marks = np.array([random.randint(0, 100)
                      for i in range(len(names))])

    # Create Student objects
    students = []

    for i in range(len(names)):
        student = Student(names[i], int(marks[i]))
        students.append(student)

    # Convert into Pandas DataFrame
    data = {
        "Name": [s.name for s in students],
        "Marks": [s.marks for s in students],
        "Grade": [s.get_grade() for s in students]
    }

    df = pd.DataFrame(data)

    # Display results
    print("EXAM RESULTS")
    print(df)

    # Calculate statistics using math module
    average = math.fsum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("\nStatistics")
    print("Average Marks:", average)
    print("Highest Marks:", highest)
    print("Lowest Marks:", lowest)

    # Save report to file
    with open("student_report.txt", "w") as file:
        file.write("STUDENT EXAM REPORT\n")
        file.write(df.to_string())
        file.write("\n\nAverage Marks: " + str(average))
        file.write("\nHighest Marks: " + str(highest))
        file.write("\nLowest Marks: " + str(lowest))

    print("\nReport saved successfully!")

except ValueError:
    print("Invalid value entered!")

except ZeroDivisionError:
    print("Cannot calculate average!")

except Exception as e:
    print("Error:", e)
