numbers = input().split(", ")
final_integers_list = []

for num in numbers:
    if num == '0':
        numbers.remove(num)
        numbers.append(num)

final_integers_list = map(int, numbers)

print(final_integers_list)
