elements = input().split(" ")
bakery = {}

for e in range(0, len(elements), 2):
    key = elements[e]
    value = elements[e + 1]
    bakery[key] = int(value)

print(bakery)
