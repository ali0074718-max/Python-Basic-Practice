with open("demo.txt", "w") as file:
    file.write("Using context manager!")

with open("demo.txt", "r") as file:
    data = file.read()
    print(data)

