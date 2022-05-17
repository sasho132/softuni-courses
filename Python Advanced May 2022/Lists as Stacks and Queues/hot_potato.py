from collections import deque

kids_queue = deque(input().split())

num = int(input())

while len(kids_queue) > 1:
    kids_queue.rotate(-num)
    print(f"Removed {kids_queue.pop()}")

print(f"Last is {kids_queue.pop()}")
