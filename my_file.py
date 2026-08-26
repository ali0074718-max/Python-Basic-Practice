# write file
file = open("data.txt", "w")
file.write("Hello! This is my first file")
file.close()

# Read File
file = open("data.txt", "r")
print(file.read())
file.close()

# Append file
file = open("data.txt", "a")
file.write("\n New line Added!")
file.close()

file = open("data.txt", "r")
print(file.read())
file.close()

file = open("data.txt", "w")
file.write("Well come")
file.close()

file = open("data.txt", "a")
file.write("\n in Pakistan")
file.close()