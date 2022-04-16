numbers = list(map(lambda x: int(x), input().split(", ")))
even_number_indexes = []

for index, number in enumerate(numbers):
    if number % 2 == 0:
        even_number_indexes.append(index)

print(even_number_indexes)
