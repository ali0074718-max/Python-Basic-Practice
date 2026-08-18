class A:
    def showdata(self):
        print("I am in clas A")
class B(A):
    def showdata(self):
        print("I an in class B")
obj = B()
obj.showdata()