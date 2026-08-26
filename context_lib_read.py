from contextlib import ExitStack
with ExitStack() as stack:
    file1 = stack.enter_context(open("file1.txt", "r"))
    file2 = stack.enter_context(open("file2.txt", "r"))

    print("Content of file1:", file1.read())
    print("Content of file2:", file2.read())
