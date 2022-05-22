n = int(input())
cars_in_parking = set()

for _ in range(n):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        cars_in_parking.add(car_number)
    elif direction == 'OUT':
        cars_in_parking.discard(car_number)

if not cars_in_parking:
    print("Parking Lot is Empty")
else:
    print("\n".join(cars_in_parking))
