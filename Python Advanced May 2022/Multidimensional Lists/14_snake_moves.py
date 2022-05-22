rows, cols = [int(x) for x in input().split()]

text = input()
matrix = []
index = 0

for row in range(rows):
    row_elements = []
    for col in range(cols):
        row_elements.append(text[index % len(text)])
        index += 1

    if row % 2 == 0:
        print(*row_elements, sep='')
    else:
        print(*reversed(row_elements), sep='')
