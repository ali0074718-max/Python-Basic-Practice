from pathlib import Path
file_path = Path("modern_file.txt")
with file_path.open("r") as f:
    content = f.read()
    print(content)