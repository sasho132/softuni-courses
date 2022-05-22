quantity = int(input())
days_left = int(input())

ornament_set_price = 2
tree_skit_price = 5
tree_garlands_price = 3
tree_lights_price = 15
christmas_spirit = 0
total_cost = 0

if days_left % 10 == 0:
    christmas_spirit -= 30
for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ornament_set_price * quantity
        christmas_spirit += 5
    if day % 3 == 0:
        total_cost += (tree_skit_price + tree_garlands_price) * quantity
        christmas_spirit += 13
    if day % 5 == 0:
        total_cost += tree_lights_price * quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        total_cost += tree_skit_price + tree_garlands_price + tree_lights_price
        christmas_spirit -= 20

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")
