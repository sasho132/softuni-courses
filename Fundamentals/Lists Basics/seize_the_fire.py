cells_on_fire = input().split("#")
water_value = int(input())
final_list = []
total_fire = 0
total_effort = 0

for cells in cells_on_fire:
    current_cell_list = cells.split("=")
    for index, cell in enumerate(current_cell_list):
        if 'High' in cell and 81 <= int(current_cell_list[index + 1]) <= 125 or \
            'Medium' in cell and 51 <= int(current_cell_list[index + 1]) <= 80 or \
                'Low' in cell and 1 <= int(current_cell_list[index + 1]) <= 50:
            if water_value - int(current_cell_list[index + 1]) >= 0:
                final_list.append(current_cell_list[index + 1])
                water_value -= int(current_cell_list[index + 1])
                total_fire += int(current_cell_list[index + 1])
                total_effort += int(current_cell_list[index + 1]) * 0.25
            else:
                continue
        current_cell_list = []

print('Cells:')
for cell_value in final_list:
    print(f" -{cell_value}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
