try:
    print("Running code....")
except:
    print("Error found!")
else:
    print("No error found!")
finally:
    print("Done!")
    print()

# Program 2
filename = "my_info.txt"
try:
    print("Attempting to open the file...")
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("Success! File found and here is the content!")
    print(content)
finally:
    print("Process completed, closing the program.")
