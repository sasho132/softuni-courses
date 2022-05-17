from collections import deque

num = int(input())
pumps = deque()

for _ in range(num):
    pumps.append([int(x) for x in input().split()])

for current_pump in range(len(pumps)):
    is_failed = False
    tank = 0

    for fuel, distance in pumps:
        tank += fuel

        if distance > tank:
            is_failed = True
            break
        else:
            tank -= distance

    if is_failed:
        pumps.append(pumps.popleft())
    else:
        print(current_pump)
        break
