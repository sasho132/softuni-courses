rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for x in range(rows)]
counter = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        submatrix = [matrix[row][col], matrix[row][col + 1],
                     matrix[row + 1][col], matrix[row + 1][col + 1]
                     ]
        if matrix[row][col] == matrix[row][col + 1] == \
                matrix[row + 1][col] == matrix[row + 1][col + 1]:
            counter += 1

print(counter)
