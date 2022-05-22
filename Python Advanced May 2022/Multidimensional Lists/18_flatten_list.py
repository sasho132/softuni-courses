s = [x.strip() for x in input().split("|")]

matrix = []

for i in reversed(s):
    matrix.append([x for x in i.split()])

for row in matrix:
    print(*row, end=' ')
