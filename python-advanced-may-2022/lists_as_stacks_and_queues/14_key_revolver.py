from collections import deque

prise_of_one_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
bullet_counter = 0

while bullets:
    if bullet_counter == gun_barrel_size:
        print('Reloading!')
        bullet_counter = 0
    if len(locks) <= 0:
        break
    current_bullet = bullets.pop()
    bullet_counter += 1
    intelligence_value -= prise_of_one_bullet
    lock = locks[0]
    if current_bullet <= lock:
        locks.popleft()
        print('Bang!')
    else:
        print('Ping!')

if len(locks) <= 0:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
