def invalid_index(row, col, matrix_rows, matrix_cols):
    return 0 > row or 0 > col or row >= matrix_rows or col >= matrix_cols


rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

while True:
    line = input()

    if line == 'END':
        break

    command = line.split()

    if command[0] != 'swap' or len(command) > 5:
        print("Invalid input!")
        continue

    row1, col1, row2, col2 = [int(x) for x in command[1:]]

    if invalid_index(row1, col1, rows, columns) or invalid_index(row2, col2, rows, columns):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=' ')
