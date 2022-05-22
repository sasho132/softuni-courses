def out_of_neighborhood(row, col, size):
    return 0 <= row < size and 0 <= col < size


def santa_move(row, col, matrix, direction):
    if direction == 'up':
        if out_of_neighborhood(row - 1, col, len(matrix)):
            return row - 1, col
    elif direction == 'down':
        if out_of_neighborhood(row + 1, col, len(matrix)):
            return row + 1, col
    elif direction == 'right':
        if out_of_neighborhood(row, col + 1, len(matrix)):
            return row, col + 1
    elif direction == 'left':
        if out_of_neighborhood(row, col - 1, len(matrix)):
            return row, col - 1


presents_count = int(input())
size = int(input())
neighborhood = []
total_good_kids = 0
presents_to_good_kids = 0

santa_row = 0
santa_col = 0

for row in range(size):
    row_data = [x for x in input().split()]
    neighborhood.append(row_data)
    for col in range(size):
        if neighborhood[row][col] == 'S':
            santa_row = row
            santa_col = col
        elif neighborhood[row][col] == 'V':
            total_good_kids += 1
 
while True:
    command = input()
    if command == "Christmas morning":
        break
    direction = command
    
    neighborhood[santa_row][santa_col] = '-'
    santa_row, santa_col = santa_move(santa_row, santa_col, neighborhood, direction)

    if neighborhood[santa_row][santa_col] == 'V':
        presents_count -= 1
        presents_to_good_kids += 1
    elif neighborhood[santa_row][santa_col] == 'C':
        if neighborhood[santa_row][santa_col - 1] == 'V':
            presents_to_good_kids += 1
            presents_count -= 1
        elif neighborhood[santa_row][santa_col - 1] == 'X':
            presents_count -= 1
        neighborhood[santa_row][santa_col - 1] = '-'

        if neighborhood[santa_row][santa_col + 1] == 'V':
            presents_to_good_kids += 1
            presents_count -= 1
        elif neighborhood[santa_row][santa_col + 1] == 'X':
            presents_count -= 1
        neighborhood[santa_row][santa_col + 1] = '-'

        if neighborhood[santa_row + 1][santa_col] == 'V':
            presents_to_good_kids += 1
            presents_count -= 1
        elif neighborhood[santa_row + 1][santa_col] == 'X':
            presents_count -= 1
        neighborhood[santa_row + 1][santa_col] = '-'

        if neighborhood[santa_row - 1][santa_col] == 'V':
            presents_to_good_kids += 1
            presents_count -= 1
        elif neighborhood[santa_row - 1][santa_col] == 'X':
            presents_count -= 1
        neighborhood[santa_row - 1][santa_col] = '-'

    neighborhood[santa_row][santa_col] = 'S'

    if presents_count == 0 or presents_to_good_kids == total_good_kids:
        break

if presents_count == 0 and presents_to_good_kids < total_good_kids:
    print("Santa ran out of presents!")
for r in neighborhood:
    print(*r, sep=' ')
if presents_to_good_kids == total_good_kids:
    print(f"Good job, Santa! {total_good_kids} happy nice kid/s.")
else:
    print(f"No presents for {total_good_kids - presents_to_good_kids} nice kid/s.")
