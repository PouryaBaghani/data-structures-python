n = int(input("enter n for a n*n Matrix\n"))
matrix = []
for i in range (n):
    row = []

    for j in range (n):
        value = int(input(f"enter number for row {i} and col {j}\n"))
        row += [value]

    matrix += [row]

print("matrix:")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " ")
    print()

sparseMatrix = []
for i in range (n):
    for j in range (n):
        if matrix[i][j] != 0:
            sparseMatrix += [(i, j, matrix[i][j])]
            
print("spars:")
for item in sparseMatrix:
    print(f"row: {item[0]} col: {item[1]} value: {item[2]}")