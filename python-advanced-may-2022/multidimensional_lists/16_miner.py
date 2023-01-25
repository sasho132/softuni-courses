def player_move(row, col, command):
    if command == 'left':
        col -= 1
    elif command == 'right':
        col += 1
    elif command == 'up':
        row -= 1
    elif command == 'down':
        row += 1

    return row, col


field_size = int(input())
commands = [x for x in input().split()]
field = []

total_coal = 0
player_row = 0
player_col = 0
coal_is_collected = False
game_is_over = False

for row in range(field_size):
    current_row = [x for x in input().split()]
    field.append(current_row)
    for col in range(len(field[row])):
        if field[row][col] == 'c':
            total_coal += 1
        if field[row][col] == 's':
            player_row = row
            player_col = col

for command in commands:
    move_row, move_col = player_move(player_row, player_col, command)

    if 0 > move_row or move_row >= field_size or 0 > move_col or move_col >= field_size:
        continue

    player_row, player_col = move_row, move_col

    if field[player_row][player_col] == 'e':
        game_is_over = True
        break
    if field[player_row][player_col] == 'c':
        total_coal -= 1
        field[player_row][player_col] = '*'

    if total_coal == 0:
        coal_is_collected = True
        break

if coal_is_collected:
    print(f"You collected all coal! ({player_row}, {player_col})")

elif game_is_over:
    print(f"Game over! ({player_row}, {player_col})")

else:
    print(f"{total_coal} pieces of coal left. ({player_row}, {player_col})")
