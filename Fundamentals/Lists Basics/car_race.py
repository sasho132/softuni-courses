times_list = input().split(" ")
left_car_time = 0
right_car_time = 0

finish_line = len(times_list) // 2

for left_side in times_list[:finish_line]:
    if left_side == "0":
        left_car_time *= 0.80
    else:
        left_car_time += int(left_side)

for right_side in times_list[len(times_list):finish_line:- 1]:
    if right_side == "0":
        right_car_time *= 0.80
    else:
        right_car_time += int(right_side)

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")
