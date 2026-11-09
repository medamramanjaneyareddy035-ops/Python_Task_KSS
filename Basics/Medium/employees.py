#* List of Dictionaries: Given the following data:
 

employees = [
    {"name": "John", "age": 25, "salary": 30000},
    {"name": "Alice", "age": 30, "salary": 50000},
    {"name": "Bob", "age": 28, "salary": 40000},
    {"name": "David", "age": 35, "salary": 60000}
]

# 1. Find the employee with the highest salary
highest_salary = max(employees, key=lambda emp: emp["salary"])
print("Highest Salary Employee:", highest_salary)

# 2. Filter employees whose salary is greater than 35,000
high_earners = [emp for emp in employees if emp["salary"] > 35000]
print("Employees earning more than 35000:", high_earners)

# 3. Calculate the average salary
average_salary = sum(emp["salary"] for emp in employees) / len(employees)
print("Average Salary:", average_salary)

# 4. Create a list containing only employee names
employee_names = [emp["name"] for emp in employees]
print("Employee Names:", employee_names)
