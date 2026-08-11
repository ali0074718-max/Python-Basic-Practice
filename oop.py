class DemoClass:
    a = 10
    def showvalue(self):
        print(10+9)
obj = DemoClass()
obj.showvalue()
print(obj.a)
print()

# Method 2
class show:
    a = 10
    def num(self):
        print(self.a)
obj1 = show()
obj1.num()
print()

#OOP (Method and Constructor)
class car:
    def __init__(self, brand, color):  # Constructor
        self.brand = brand
        self.color = color
# Creat Method
    def drive(self):
        print(f"{self.brand} car is draving")
# Object Creation
car1 = car("BMW", "red")
car2 = car("Alto", "white")
print(car1.brand)
car2.drive()
print()

# Multiple
class MathOperation:
    def mul(self, a , b):
        print(a * b)
calc = MathOperation()
calc.mul(10,9)
print()

# Student detail
class Student:
    def __init__(self, name, roll_no, course ):
        self.name = name
        self.roll_no = roll_no
        self.course = course
    def showdetail(self):
        print(f"{self.name} , {self.roll_no} , {self.course}")
student1 = Student("Ali", 18, "Python")
student2 = Student("Ahmad", 20, "C++" )
student1.showdetail()
print(f"{student2.name} , {student2.roll_no} , {student2.course}")



