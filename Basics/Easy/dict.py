#* Dictionary Operations: Create a dictionary containing student names and marks. Add a new student, update an existing student's marks, and print all student details.

students = {
    "ram" : 80,
    "ravi": 90,
    "mahesh": 95
 }
# Add a new student data
students ["rohit"] = 95
#Update existing students marks

students["ram"] = 95

#Print all students data
for name,marks in students.items():
    print(name,":",marks)
