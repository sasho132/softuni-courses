def index_validation(inx_row, inx_col, matrix):
    return 0 <= inx_row < len(matrix) and 0 <= inx_col < len(matrix)


def bomb_explosion(row, col, matrix_data):
    bomb_value = matrix_data[row][col]

    if index_validation(row - 1, col, matrix_data) and matrix_data[row - 1][col] > 0:
        matrix_data[row - 1][col] -= bomb_value
    if index_validation(row - 1, col - 1, matrix_data) and matrix_data[row - 1][col - 1] > 0:
        matrix_data[row - 1][col - 1] -= bomb_value
    if index_validation(row - 1, col + 1, matrix_data) and matrix_data[row - 1][col + 1] > 0:
        matrix_data[row - 1][col + 1] -= bomb_value
    if index_validation(row, col + 1, matrix_data) and matrix_data[row][col + 1] > 0:
        matrix_data[row][col + 1] -= bomb_value
    if index_validation(row, col - 1, matrix_data) and matrix_data[row][col - 1] > 0:
        matrix_data[row][col - 1] -= bomb_value
    if index_validation(row + 1, col, matrix_data) and matrix_data[row + 1][col] > 0:
        matrix_data[row + 1][col] -= bomb_value
    if index_validation(row + 1, col + 1, matrix_data) and matrix_data[row + 1][col + 1] > 0:
        matrix_data[row + 1][col + 1] -= bomb_value
    if index_validation(row + 1, col - 1, matrix_data) and matrix_data[row + 1][col - 1] > 0:
        matrix_data[row + 1][col - 1] -= bomb_value

    matrix_data[row][col] = 0

    return matrix_data


n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs_indexes = [x for x in input().split()]

for indexes in bombs_indexes:
    bomb_row, bomb_col = [int(x) for x in indexes.split(',')]
    if matrix[bomb_row][bomb_col] <= 0:
        continue

    matrix = bomb_explosion(bomb_row, bomb_col, matrix)

active_cells = 0
total_sum = 0
for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            active_cells += 1
            total_sum += matrix[r][c]

print(f"Alive cells: {active_cells}")
print(f"Sum: {total_sum}")
for matrix_row in matrix:
    print(*matrix_row, sep=' ')
