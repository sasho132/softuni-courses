number_of_rooms = int(input())
free_chairs = 0
is_chairs_enough = True

for room in range(1, number_of_rooms + 1):
    current_room = input().split(" ")
    chairs = current_room[0]
    people = int(current_room[1])
    diff = abs(people - len(chairs))
    free_chairs += diff

    if len(chairs) < people:
        print(f"{diff} more chairs needed in room {room}")
        is_chairs_enough = False
        continue

if is_chairs_enough:
    print(f"Game On, {free_chairs} free chairs left")
