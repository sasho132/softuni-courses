events = input().split("|")
energy = 100
gained_energy = 0
coins = 100
is_closed = False

for current_command in events:
    temp_event = current_command.split("-")
    current_event = temp_event[0]
    current_value = int(temp_event[1])
    if current_event == 'rest':
        if current_value + energy <= 100:
            energy += current_value
            gained_energy += current_value
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        else:
            print(f"You gained 0 energy.")
            print(f"Current energy: {energy}.")
        gained_energy = 0
    elif current_event == 'order':
        order_energy = 30
        if energy - order_energy >= 0:
            energy -= order_energy
            coins += current_value
            print(f"You earned {current_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        ingredient = current_event
        ingredient_cost = current_value
        if ingredient_cost < coins:
            coins -= ingredient_cost
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
