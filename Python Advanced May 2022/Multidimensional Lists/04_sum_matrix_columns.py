rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for col in range(columns):
    col_sum = 0
    for row in range(rows):
        col_sum += matrix[row][col]
    print(col_sum)
