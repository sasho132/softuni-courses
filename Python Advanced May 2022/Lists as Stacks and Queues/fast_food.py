from collections import deque

quantity_of_food = int(input())
orders_queue = deque(map(int, input().split()))

if orders_queue:
    print(max(orders_queue))

while orders_queue:
    current_order = orders_queue[0]
    if quantity_of_food - current_order >= 0:
        quantity_of_food -= current_order
        orders_queue.popleft()
    else:
        break

if not orders_queue:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(map(str, orders_queue))}")
