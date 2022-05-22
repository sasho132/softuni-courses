matrix = [[int(x) for x in input().split(', ')] for x in range(int(input()))]

primary_diagonal = []
secondary_diagonal = []
primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for col in range(len(matrix) - 1, -1, -1):
    secondary_diagonal.append(matrix[(len(matrix) - 1) - col][col])
    secondary_diagonal_sum += matrix[(len(matrix) - 1) - col][col]

for num in range(len(matrix)):
    primary_diagonal.append(matrix[num][num])
    primary_diagonal_sum += matrix[num][num]

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {primary_diagonal_sum}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {secondary_diagonal_sum}")
