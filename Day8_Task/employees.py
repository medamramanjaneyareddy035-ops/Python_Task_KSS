# Employee Salary Management System 
'''A company stores employee data in a file employees.txt in the format: 
EmployeeName Salary 
Example: 
Ramesh 25000 
Sita 30000 
Arun 28000 
Write a Python program that: 
● Reads employee data from the file 
● Displays all employee details 
● Finds the employee with the highest salary 
● Appends a new employee record to the file.
'''# Read employee data from file
file = open("employees.txt", "r")

employees = []

for line in file:
    name, salary = line.split()
    employees.append((name, int(salary)))

file.close()

# Display all employee details
print("Employee Details:")
for name, salary in employees:
    print(name, salary)

# Find employee with highest salary
highest = max(employees, key=lambda x: x[1])

print("\nEmployee with Highest Salary:")
print("Name:", highest[0])
print("Salary:", highest[1])

# Append new employee record
file = open("employees.txt", "a")

name = input("\nEnter Employee Name: ")
salary = int(input("Enter Salary: "))

file.write(name + " " + str(salary) + "\n")
file.close()

print("Employee record added successfully!")
