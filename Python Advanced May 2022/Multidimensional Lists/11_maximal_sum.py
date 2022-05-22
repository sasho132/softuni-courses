rows, columns = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for x in range(rows)]
max_sum = -99999999999999999
max_submatrix = []

for row in range(rows - 2):
    for col in range(columns - 2):
        submatrix = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                     matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                     matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]
                     ]
        if sum(submatrix) > max_sum:
            max_sum = sum(submatrix)
            max_submatrix = submatrix

print(f"Sum = {max_sum}")
print(f"{max_submatrix[0]} {max_submatrix[1]} {max_submatrix[2]}")
print(f"{max_submatrix[3]} {max_submatrix[4]} {max_submatrix[5]}")
print(f"{max_submatrix[6]} {max_submatrix[7]} {max_submatrix[8]}")
