num = int(input())
result = []
odds = set()
evens = set()

for row in range(1, num + 1):
    name = input()

    name_sum = sum([ord(x) for x in name]) /row
    if name_sum % 2 == 0:
        evens.add(int(name_sum))
    else:
        odds.add(int(name_sum))

