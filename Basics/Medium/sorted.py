#* Dictionary Sorting: Given a dictionary:
 
'''    ```python
    students = {
        "Rahul": 85,
        "Amit": 92,
        "Priya": 78,
        "Sneha": 95
    }
    ```
 
    Sort the dictionary based on marks in descending order and print the top two students.
    
'''
students = {
        "Rahul": 85,
        "Amit": 92,
        "Priya": 78,
        "Sneha": 95
    }
result = sorted(students.items(),key=lambda X: X[1], reverse=True)
print("Top 2 students:")

for name,marks in result[:2]:
    print(name,marks)
