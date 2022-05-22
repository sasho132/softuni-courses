def add_user(forces_dictionary, add_to_side, user_to_add):
    for current_side, current_user in forces_dictionary.items():
        if user_to_add in current_user:
            return forces_dictionary

    if add_to_side not in forces_dictionary:
        forces_dictionary[add_to_side] = []
    forces_dictionary[add_to_side].append(user_to_add)

    return forces_dictionary


def change_side(forces_dictionary, side_to_change, user_to_change):
    for current_side in forces_dictionary:
        if user_to_change in forces_dictionary[current_side]:
            if len(forces_dictionary[current_side]) > 1:
                forces_dictionary[current_side].pop(user_to_change)
                break
            else:
                del forces_dictionary[current_side]
                break

    forces_dictionary = add_user(forces_dictionary, side_to_change, user_to_change)

    print(f"{user_to_change} joins the {side_to_change} side!")

    return forces_dictionary


forces = {}

line = input()
while line != 'Lumpawaroo':
    if '|' in line:
        side, user = line.split(" | ")
        forces = add_user(forces, side, user)
    else:
        user, side = line.split(" -> ")
        forces = change_side(forces, side, user)

    line = input()

for side, users in forces.items():
    print(f"Side: {side}, Members: {len(users)}")
    for usr in users:
        print(f"! {usr}")
