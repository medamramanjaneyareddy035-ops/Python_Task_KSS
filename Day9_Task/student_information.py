# Student Information System (Class & Object) 
'''A school wants a program to store student details. Create a Student class with 
attributes such as name, roll number, and marks. Create objects for at least three 
students and display their details.
'''
class student:
    def display(self, name, rollno, marks):
        print("Name:", name)
        print("Roll Number:",rollno)
        print("marks:",marks)

s1 = student()
s1.display("Ram", 101, 90)

s2 = student()
s2.display("Rohit", 102, 80)

s3 = student()
s3.display("mahesh", 103, 70)

s4 = student()
s4.display("ravi", 104, 85)

           
