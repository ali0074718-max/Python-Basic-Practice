class Area:
    def find_area(self, x = None , y = None):
        if x != None and y != None:
            print("Area of rectangular:", (x * y))
        elif x != None:
            print("Area of square:", (x * x))
        else:
            print("Nothing to find")
obj = Area()
obj.find_area()
obj.find_area(10)
obj.find_area(10,20)

