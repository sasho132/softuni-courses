numbers = input().split(" ")
int_list = []

for num in numbers:
    int_list.append(int(num))

smallest_number = min(int_list)
biggest_number = max(int_list)
sum_of_numbers = sum(int_list)

print(f"The minimum number is {smallest_number}")
print(f"The maximum number is {biggest_number}")
print(f"The sum number is: {sum_of_numbers}")
