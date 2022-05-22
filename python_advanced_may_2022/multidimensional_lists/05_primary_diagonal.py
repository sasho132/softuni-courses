n = int(input())
matrix = []

for _ in range(n):
     matrix.append([int(el) for el in input().split()])

res = 0
for num in range(n):
     res += matrix[num][num]

print(res)
