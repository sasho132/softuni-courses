def valid_index(row, col, board_size):
    return 0 <= row and row < board_size and 0 <= col and col < board_size


def knight_index(row, col, board):
    return board[row][col] == 'K'


def knights_move(row, col, board):
    counter = 0

    if valid_index(row - 1, col - 2, board_size) and knight_index(row - 1, col - 2, board):
        counter += 1
    if valid_index(row - 1, col + 2, board_size) and knight_index(row - 1, col + 2, board):
        counter += 1
    if valid_index(row - 2, col - 1, board_size) and knight_index(row - 2, col - 1, board):
        counter += 1
    if valid_index(row - 2, col + 1, board_size) and knight_index(row - 2, col + 1, board):
        counter += 1

    if valid_index(row + 1, col - 2, board_size) and knight_index(row + 1, col - 2, board):
        counter += 1
    if valid_index(row + 1, col + 2, board_size) and knight_index(row + 1, col + 2, board):
        counter += 1
    if valid_index(row + 2, col - 1, board_size) and knight_index(row + 2, col - 1, board):
        counter += 1
    if valid_index(row + 2, col + 1, board_size) and knight_index(row + 2, col + 1, board):
        counter += 1

    return counter


board_size = int(input())
board = []
knights_counter = 0

for _ in range(board_size):
    board.append([x for x in input()])

while True:
    knights = {}

    for row in range(board_size):
        for col in range(board_size):
            if board[row][col] == "0":
                continue

            if knights_move(row, col, board) > 0:
                current_knight_count = knights_move(row, col, board)
                knights[(row, col)] = current_knight_count

    if len(knights) == 0:
        break

    knight_row = 0
    knight_col = 0
    knight_highest_score = 0
    for key, value in knights.items():
        if value > knight_highest_score:
            knight_highest_score = value
            knight_row = int(key[0])
            knight_col = int(key[1])

    board[knight_row][knight_col] = '0'
    knights_counter += 1

print(knights_counter)
