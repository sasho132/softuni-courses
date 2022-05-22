from collections import deque

green_light = int(input())
free_window = int(input())
cars = deque()
car_crash = False
total_cars_passed = 0

command = input()
while command != 'END' and not car_crash:
    if command != 'green':
        cars.append(command)
    else:
        car_ch_counter = 0
        light_counter = green_light
        while len(cars) > 0 and car_ch_counter < green_light and not car_crash:
            current_car = cars.popleft()
            for car_ch in current_car:
                car_ch_counter += 1
                if car_ch_counter > green_light + free_window:
                    car_crash = True
                    print("A crash happened!")
                    print(f"{current_car} was hit at {car_ch}.")
                    break
            total_cars_passed += 1

    command = input()

if not car_crash:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")
