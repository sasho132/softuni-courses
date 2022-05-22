numbers = [int(x) for x in input().split()]

target_number = int(input())
iterations_counter = 0
pairs = set()

for n1 in range(len(numbers)):
    for n2 in range(n1 + 1, len(numbers)):
        iterations_counter += 1
        if numbers[n1] + numbers[n2] == target_number:
            current_pair = (numbers[n1], numbers[n2])
            pairs.add(current_pair)
            print(f"{numbers[n1]} + {numbers[n2]} = {target_number}")

print(f"Iterations done: {iterations_counter}")

[print(x) for x in pairs]
