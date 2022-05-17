from collections import deque

supermarket_queue = deque()

name = input()
while not name == 'End':
    if name == 'Paid':
        while len(supermarket_queue):
            print(supermarket_queue.popleft())
    else:
        supermarket_queue.append(name)
    name = input()

print(f"{len(supermarket_queue)} people remaining.")
