n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

line = input().split()
while line[0] != "END":
    command = line[0]
    row = int(line[1])
    col = int(line[2])
    value = int(line[3])

    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")
    
    line = input().split()

for current_row in matrix:
    print(*current_row, sep=" ")
