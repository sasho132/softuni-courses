from unicodedata import name


num = int(input())
names = set()

for _ in range(num):
    names.add(input())

print('\n'.join(names))
