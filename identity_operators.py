x = 10
y = 10
print("x is y", x is y) #same memory location
print("x Memory ID:", id(x))
print("y Memory ID:", id(y))
# is not
print("x is nor y: ", x is not y)

# List with same value. (Different Memory locations)
list1 = [10,20,30,40]
list2 = [10,20,30,40]
print("list1 is list2:", list1 is list2) #Value same but memory address differnt
print("list1 is not list2:", list1 is not list2)
#Check Memory Address of Lists
print("list1 Memory ID:", id(list1))
print("list2 Memort ID:", id(list2))
