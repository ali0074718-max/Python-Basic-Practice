from contextlib import ExitStack
with ExitStack() as stack:
    file1 = stack.enter_context(open("File1.txt", "w"))
    file2 = stack.enter_context(open("File2.txt", "w"))

    file1.write("Hello from file1")
    # file2.write("Hello from file2")
    print("Done")
