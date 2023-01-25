def player_move(command, row, col):
    if command == "L":
        col -= 1
    elif command == "R":
        col += 1
    elif command == "U":
        row -= 1
    elif command == "D":
        row += 1
    return row, col


def outside_field(row, col, field_rows, field_cols):
    return 0 > row or row >= field_rows or 0 > col or col >= field_cols


rows, cols = [int(x) for x in input().split()]

field = []
player_row = 0
player_col = 0
bunnies = set()

for row in range(rows):
    row_data = list(input())
    field.append(row_data)
    for col in range(len(row_data)):
        if field[row][col] == "P":
            player_row, player_col = row, col
        if field[row][col] == "B":
            bunnies.add(f"{row} {col}")

commands = list(input())
game_won = False
dead = False

field[player_row][player_col] = "."
for command in commands:

    move_row, move_col = player_move(command, player_row, player_col)
    if outside_field(move_row, move_col, rows, cols):
        game_won = True
    else:
        if field[move_row][move_col] == "B":
            dead = True
        player_row, player_col = move_row, move_col

    bunnies_spread = set()

    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]

        if not outside_field(bunny_row, bunny_col - 1, rows, cols):
            bunnies_spread.add(f"{bunny_row} {bunny_col - 1}")
            field[bunny_row][bunny_col - 1] = "B"

        if not outside_field(bunny_row, bunny_col + 1, rows, cols):
            bunnies_spread.add(f"{bunny_row} {bunny_col + 1}")
            field[bunny_row][bunny_col + 1] = "B"

        if not outside_field(bunny_row - 1, bunny_col, rows, cols):
            bunnies_spread.add(f"{bunny_row - 1} {bunny_col}")
            field[bunny_row - 1][bunny_col] = "B"

        if not outside_field(bunny_row + 1, bunny_col, rows, cols):
            bunnies_spread.add(f"{bunny_row + 1} {bunny_col}")
            field[bunny_row + 1][bunny_col] = "B"

    bunnies = bunnies.union(bunnies_spread)

    if field[player_row][player_col] == "B":
        dead = True

    if dead or game_won:
        break

for row in field:
    print(*row, sep="")

if game_won:
    print(f"won: {player_row} {player_col}")

elif dead:
    print(f"dead: {player_row} {player_col}")
