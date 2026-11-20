#University Staff Management (Hierarchical Inheritance) 
'''A university has different staff types such as Professor, LabAssistant, and 
Administrator. All inherit from a base class Staff. Implement hierarchical inheritance 
to manage and display their information.
'''
class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


class Professor(Staff):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject

    def display(self):
        super().display()
        print("Subject:", self.subject)


class LabAssistant(Staff):
    def __init__(self, name, salary, lab):
        super().__init__(name, salary)
        self.lab = lab

    def display(self):
        super().display()
        print("Lab:", self.lab)


class Administrator(Staff):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


p = Professor("Ram", 50000, "Python")
l = LabAssistant("Ravi", 25000, "Computer Lab")
a = Administrator("Kiran", 40000, "HR")

p.display()
l.display()
a.display()
