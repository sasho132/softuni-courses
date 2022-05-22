rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

evens = [[x for x in rows if x % 2 == 0] for rows in matrix]
print(evens)
