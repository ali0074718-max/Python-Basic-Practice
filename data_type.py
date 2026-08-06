# Numeric Types
num1 = 25
num2 = 15.5
num3 = 2 + 5j
print("Integer:", num1, "| Type:", type(num1))
print("Float: ", num2, "| Type:", type(num2))
print("Complex: ", num3, "| Type:", type(num3))

# Text and Boolean Types
text = "Python Programming"
multi_str = """ Hello 
                        World"""
b = True
print("String:", text, "| Type:", type(text))
print("Triple Quotes:", multi_str, "| Type:", type(multi_str))
print("Boolean:", b, "| Type:", type(b))

# sequence Type
l = [10, 20, "apple", 2.5]
t = (20, 30, 40, "Hello")
print("List:", l, "| Type:", type(l))
print("Tuple:", t, "| Type:", type(t))

# Maping and set
d = {"name" : "Ali", "age" : 20}
s = {1,2,3,4,}
s.add(5)
fs = frozenset([1,2,3,4,5])
print('Dictionary:', d, "| Type:",type(d))
print("Set:", s, "| Set:", type(s))
print("Frozenset:", fs, "| Type:", type(fs))