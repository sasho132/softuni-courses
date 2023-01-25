num = int(input())
result = []
odds = set()
evens = set()

for row in range(1, num + 1):
    name = input()

    name_sum = sum(ord(x) for x in name) / row
    if int(name_sum) % 2 == 0:
        evens.add(int(name_sum))
    else:
        odds.add(int(name_sum))

odds_total = sum(odds)
evens_total = sum(evens)
result = ''

if odds_total == evens_total:
    result = odds.union(evens)

elif odds_total > evens_total:
    result = odds.difference(evens)

elif evens_total > odds_total:
    result = odds.symmetric_difference(evens)

print(', '.join(str(x) for x in result))
