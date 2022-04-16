def shoot(targets, index, value):
    targets[index] -= value
    if targets[index] <= 0:
        targets.pop(index)
    return targets


def add(targets, index, value):
    targets.insert(index, value)
    return targets


def strike(targets, index, value):
    left_radius = targets[0:index - value]
    right_radius = targets[index + value + 1::]
    targets = left_radius + right_radius
    return targets


sequence_of_targets = [int(target) for target in input().split()]

command = input().split()
while command[0] != "End":
    target_index = int(command[1])
    target_value = int(command[2])
    if command[0] == "Shoot":
        if 0 <= target_index < len(sequence_of_targets):
            target_shoot = shoot(sequence_of_targets, target_index, target_value)
    elif command[0] == "Add":
        if 0 <= target_index < len(sequence_of_targets):
            target_add = add(sequence_of_targets, target_index, target_value)
        else:
            print("Invalid placement!")
    elif command[0] == "Strike":
        if 0 <= target_index - target_value < len(sequence_of_targets) and \
                0 <= target_index + target_value < len(sequence_of_targets):
            sequence_of_targets = strike(sequence_of_targets, target_index, target_value)
        else:
            print("Strike missed!")
    command = input().split()

targets_str = map(str, sequence_of_targets)
print("|".join(targets_str))
