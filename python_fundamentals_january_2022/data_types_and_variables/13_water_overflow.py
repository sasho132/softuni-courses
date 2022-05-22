number_of_lines = int(input())
tank_capacity_in_l = 255
litters_in_tank = 0

for i in range(0, number_of_lines):
    litters_of_watter = int(input())
    if litters_of_watter + litters_in_tank > tank_capacity_in_l:
        print("Insufficient capacity!")
        continue
    litters_in_tank += litters_of_watter

print(litters_in_tank)
