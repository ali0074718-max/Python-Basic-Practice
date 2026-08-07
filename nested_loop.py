row = int(input("Enter the size of row:"))
cols = int(input("Enter the size of column:"))
matrix = []
print("Enter the elements of Matrix:")
for r in range(row):
    a = []
    for c in range(cols):
        a.append(int(input()))
    matrix.append(a)

for r in range(row):
    print("\n")
    for c in range(cols):
        print(matrix[r][c],end="\t")

