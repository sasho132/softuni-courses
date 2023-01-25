matrix = [[int(x) for x in input().split()] for x in range(int(input()))]

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for col in range(len(matrix) - 1, -1, -1):
    secondary_diagonal_sum += matrix[(len(matrix) - 1) - col][col]

for num in range(len(matrix)):
    primary_diagonal_sum += matrix[num][num]

print(abs(secondary_diagonal_sum - primary_diagonal_sum))
