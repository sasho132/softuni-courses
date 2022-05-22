parking_lot = {}

num = int(input())

for person in range(num):
    command = input().split()
    if command[0] == 'register':
        username = command[1]
        reg_plate = command[2]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = reg_plate
            print(f"{username} registered {reg_plate} successfully")

    else:
        username = command[1]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            del parking_lot[username]
            print(f"{username} unregistered successfully")

for key, value in parking_lot.items():
    print(f"{key} => {value}")
