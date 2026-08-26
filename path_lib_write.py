from pathlib import Path
file_path = Path("modern_file.txt")
with file_path.open("w") as f:
    f.write("This is modern file handling using pathlib!")
print("Done")    