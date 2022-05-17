from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles = ([int(x) for x in input().split()])

wasted_watter = 0
bottles_counter = 0

while cups_capacity:
    if len(bottles) == 0:
        break
    current_cup = cups_capacity[0]
    while current_cup > 0 and len(bottles) > 0:
        bottle = bottles.pop()
        bottles_counter += 1
        if bottle > current_cup:
            wasted_watter += bottle - current_cup
        current_cup -= bottle
        if current_cup <= 0:
            cups_capacity.popleft()

if len(cups_capacity) == 0:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
elif len(bottles) == 0:
    print(f"Cups: {' '.join([str(x) for x in cups_capacity])}")

print(f"Wasted litters of water: {wasted_watter}")
