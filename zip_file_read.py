import zipfile
with zipfile.ZipFile("my_archive.zip", "r") as zf:
    print("Files inside zip:", zf.namelist())
    with zf.open("sample.txt") as file:
        print(file.read().decode("utf-8"))
