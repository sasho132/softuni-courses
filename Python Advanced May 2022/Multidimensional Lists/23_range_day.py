def out_of_field(row, col, size):
    return 0 > row or row >= size or 0 > col or col >= size


def next_position(row, col, move_direction, count):
    if move_direction == 'up':
        return row - count, col
    elif move_direction == 'down':
        return row + count, col
    elif move_direction == 'right':
        return row, col + count
    elif move_direction == 'left':
        return row, col - count


size = 5
field = []
shooter_row = 0
shooter_col = 0
targets_count = 0
targets = targets_count

for row in range(size):
    row_data = [x for x in input().split()]
    field.append(row_data)

    for col in range(size):
        if field[row][col] == 'A':
            shooter_row = row
            shooter_col = col
        elif field[row][col] == 'x':
            targets_count += 1

field[shooter_row][shooter_col] = '.'
n = int(input())
target_hit = []
targets = targets_count

for _ in range(n):
    line = input().split()
    command = line[0]
    direction = line[1]

    if command == 'move':
        steps = int(line[2])

        new_row, new_col = next_position(shooter_row, shooter_col, direction, steps)

        if out_of_field(new_row, new_col, size) or field[new_row][new_col] != '.':
            continue

        field[shooter_row][shooter_col] = '.'
        shooter_row, shooter_col = new_row, new_col
        field[shooter_row][shooter_col] = 'A'
    else:
        bullet_row, bullet_col = shooter_row, shooter_col

        while True:

            bullet_row, bullet_col = next_position(bullet_row, bullet_col, direction, 1)

            if out_of_field(bullet_row, bullet_col, size):
                break

            if field[bullet_row][bullet_col] == 'x':
                targets -= 1
                target_hit.append([bullet_row, bullet_col])
                field[bullet_row][bullet_col] = '.'
                break

        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {targets_count} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")
print(*target_hit, sep='\n')
