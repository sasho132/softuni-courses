numbers = int(input())
num_list = []
filtered_list = []

for i in range(numbers):
    current_number = int(input())
    num_list.append(current_number)

command = input()

for number in num_list:
    if command == 'positive' and number >= 0:
        filtered_list.append(number)
    elif command == 'negative' and number < 0:
        filtered_list.append(number)
    elif command == 'even' and number % 2 == 0:
        filtered_list.append(number)
    elif command == 'odd' and number % 2 != 0:
        filtered_list.append(number)

print(filtered_list)
