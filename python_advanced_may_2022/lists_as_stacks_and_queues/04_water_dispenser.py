from collections import deque

quantity_of_water = int(input())
people = deque()

name = input()
while not name == "Start":
    people.append(name)
    name = input()

command = input()
while not command == 'End':
    if command.isdigit():
        liters_of_water = int(command)
        if quantity_of_water >= liters_of_water:
            quantity_of_water -= liters_of_water
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    else:
        refill_command = command.split()
        liters_to_refill = int(refill_command[1])
        quantity_of_water += liters_to_refill

    command = input()

print(f"{quantity_of_water} liters left")
