# Polymorphism
l = [10,20,30,40,]
print(len(l))
char = "Welcome"
print(len(char))
print()

#Method overloading
class N:
    def display(self, name=''):
        print("Welcome"+ " "+ name)
obj1 = N()
obj1.display()
obj1.display('Ali')
print()

# Method overriding
class A:
    def displayinfo(self):
        print("Hello")
class B(A):
    def displayinfo(self):
        super().displayinfo() # Super() print Parent class
        print("Ali")
obj = B()
obj.displayinfo()