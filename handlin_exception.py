filename = "my_info.txt"
name = "Ali"
age = 20
try:
    with open(filename, "r") as fin:
        print(fin.read())
except FileNotFoundError:
    print("File not found!")
    with open(filename, "w") as fout:
        fout.write(f"{name}\n{age}\n")
    with open(filename, "r") as fin:
        print(fin.read())