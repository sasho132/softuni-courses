def out_of_the_field(row_index, col_index, matrix_size):
    return 0 > row_index or row_index >= matrix_size or 0 > col_index or col_index >= matrix_size


size = int(input())

wonderland = []
alice_row = 0
alice_col = 0

for row in range(size):
    row_data = [x for x in input().split()]
    wonderland.append(row_data)

    for col in range(size):
        if wonderland[row][col] == 'A':
            alice_row = row
            alice_col = col
            break


wonderland[alice_row][alice_col] = '*'
tea_bags_counter = 0
current_row, current_col = alice_row, alice_col
alice_go_to_party = False

command = input()
while command:

    if command == 'up':
        current_row, current_col = current_row - 1, current_col

    elif command == 'down':
        current_row, current_col = current_row + 1, current_col

    elif command == 'right':
        current_row, current_col = current_row, current_col + 1

    elif command == 'left':
        current_row, current_col = current_row, current_col - 1

    if out_of_the_field(current_row, current_col, size):
        break
    if wonderland[current_row][current_col] == 'R':
        wonderland[current_row][current_col] = '*'
        break

    if wonderland[current_row][current_col] != '.' and wonderland[current_row][current_col] != '*':
        tea_bags_counter += int(wonderland[current_row][current_col])
    wonderland[current_row][current_col] = '*'

    if tea_bags_counter >= 10:
        alice_go_to_party = True
        break

    command = input()

if alice_go_to_party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for r in wonderland:
    print(*r, sep=' ')
