rows, columns = [int(el) for el in input().split(', ')]
matrix = []
total_sum = 0

for _ in range(rows):
     current_nums = [int(el) for el in input().split(', ')]
     matrix.append(current_nums)
     total_sum += sum(current_nums)

print(total_sum)
print(matrix)
