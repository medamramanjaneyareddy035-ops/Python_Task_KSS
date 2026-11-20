# Shape Area Calculator (Polymorphism) 
'''A graphics application needs to calculate the area of different shapes. Create classes 
Circle, Rectangle, and Triangle, each having an area() method. Demonstrate 
polymorphism by calling the same method for different objects.
'''
class Circle:
    def area(self):
        r = 5
        print("Circle Area:", 3.14 * r * r)

class Rectangle:
    def area(self):
        l = 5
        b = 4
        print("Rectangle area:", l * b)

class Triangle:
    def area(self):
        b = 10
        h = 5
        print("Triangle area:", 0.5 * h * b)

a = Circle()
b = Rectangle()
c = Triangle()

a.area()
b.area()
c.area()
