length_of_sets = [int(el) for el in input().split()]

n = set()
m = set()

for num1 in range(length_of_sets[0]):
    n.add(int(input()))

for num2 in range(length_of_sets[1]):
    m.add(int(input()))

res = [str(el) for el in n.intersection(m)]
print('\n'.join(res))
