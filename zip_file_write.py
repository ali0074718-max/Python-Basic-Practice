import zipfile
with zipfile.ZipFile("my_archive.zip", "w") as zf:
    with open("sample.txt", "w") as f:
        f.write("Hello inside zip file!")
    zf.write("sample.txt")
print("Zip successfully created")