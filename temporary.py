import tempfile
with tempfile.TemporaryFile(mode="w+t") as temfp:
    temp.write("Well come")
    temp.write("\n in Pakistan")
    temp.seek(0)
    print(temp.read())


