numbers = [int(number) for number in input().split(", ")]

group = 10
counter = 0

while counter < len(numbers):
    current_list = []
    for num in numbers:
        if group - 10 < num <= group:
            current_list.append(num)
            counter += 1
    print(f"Group of {group}'s: {current_list}")
    group += 10
