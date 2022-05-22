line = input().split('|')

res = []

while line:
    numbers = line.pop().split()
    for n in numbers:
        res.append(n)

print(*res, sep=' ')
