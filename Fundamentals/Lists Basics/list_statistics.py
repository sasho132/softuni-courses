numbers = int(input())
positive_number_list = []
negative_number_list = []

for number in range(numbers):
    current_number = int(input())
    if current_number >= 0:
        positive_number_list.append(current_number)
    else:
        negative_number_list.append(current_number)

positive_counter = len(positive_number_list)
negative_number_sum = sum(negative_number_list)
print(positive_number_list)
print(negative_number_list)
print(f"Count of positives: {positive_counter}")
print(f"Sum of negatives: {negative_number_sum}")
