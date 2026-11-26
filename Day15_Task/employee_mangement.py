#5. Employee Management System (OOP + File + Dict) 
'''Scenario: 
Manage employee data. 
Task: 
● Create a class Employee 
● Store employees in a dictionary 
● Save data to a file 
● Use exception handling for invalid salary input 
● Use loop to display all employees
'''
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


# Dictionary to store employees
employees = {}

try:
    n = int(input("Enter number of employees: "))

    for i in range(n):
        print("\nEnter Employee Details")

        emp_id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))

        emp = Employee(emp_id, name, salary)

        employees[emp_id] = emp

    # Save data into file
    with open("employees.txt", "w") as file:
        for emp in employees.values():
            file.write(
                f"{emp.emp_id},{emp.name},{emp.salary}\n"
            )

    print("\nEmployee Details:")

    # Display all employees
    for emp in employees.values():
        emp.display()
        print("----------------")

except ValueError:
    print("Invalid input! Please enter valid numbers.")

# Read data from file
with open("employees.txt", "r") as file:
    print("\nSaved File Data:")
    print(file.read())
