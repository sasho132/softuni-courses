import sys


def up(row, col):
    return row - 1, col


def down(row, col):
    return row + 1, col


def right(row, col):
    return row, col + 1


def left(row, col):
    return row, col - 1


def out_of_field(row, col, size):
    return 0 > row or row >= size or 0 > col or col >= size


size = int(input())

field = []
bunny_row = 0
bunny_col = 0

for row in range(size):
    row_data = [x for x in input().split()]
    field.append(row_data)

    for col in range(size):
        if field[row][col] == 'B':
            bunny_row = row
            bunny_col = col

directions = {
    'up': up,
    'down': down,
    'right': right,
    'left': left
}

best_score = -sys.maxsize
best_direction = ''

for direction, move in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_path = []
    current_score = 0

    while True:
        current_row, current_col = move(current_row, current_col)

        if out_of_field(current_row, current_col, size):
            break

        if field[current_row][current_col] == 'X':
            break

        current_path.append([current_row, current_col])
        current_score += int(field[current_row][current_col])

    if current_score > best_score and current_path:
        best_score = current_score
        best_direction = direction

    directions[direction] = current_path

print(best_direction)
print(*directions[best_direction], sep='\n')
print(best_score)
