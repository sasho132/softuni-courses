group_size = int(input())
days_of_adventure = int(input())
coins_counter = 0

for day in range(1, days_of_adventure + 1):
    current_day_coins = 50
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    current_day_coins -= group_size * 2
    if day % 3 == 0:
        current_day_coins -= group_size * 3
    if day % 5 == 0:
        current_day_coins += group_size * 20
        if day % 3 == 0:
            current_day_coins -= group_size * 2
    coins_counter += current_day_coins

coins_per_companion = int(coins_counter / group_size)
print(f"{group_size} companions received {coins_per_companion} coins each.")
