n = int(input())
matrix = []

for _ in range(n):
    matrix.append([x for x in input()])

searched_symbol = input()
res = ()
for row in range(n):
    for col in range(n):
        if matrix[row][col] == searched_symbol:
            res = (row, col)
            print(res)
            break
    if res:
        break

if not res:
    print(f"{searched_symbol} does not occur in the matrix")
