import sys

rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])

max_sum = -sys.maxsize
biggest_submatrix = []

for row in range(rows - 1):
    for col in range(columns - 1):
        submatrix = [matrix[row][col], matrix[row][col + 1],
                     matrix[row + 1][col], matrix[row + 1][col + 1]
                     ]
        submatrix_sum = sum(submatrix)
        if submatrix_sum > max_sum:
            max_sum = submatrix_sum
            biggest_submatrix = submatrix.copy()

print(biggest_submatrix[0], biggest_submatrix[1])
print(biggest_submatrix[2], biggest_submatrix[3])
print(max_sum)
