number = input()
numbers_list = []
filtered_list = []

for num in number:
    numbers_list.append(num)

for digit in range(len(numbers_list)):
    filtered_list.append(max(numbers_list))
    numbers_list.remove(max(numbers_list))

print(''.join(filtered_list))
