numbers_list = input().split()
opposite_list = []

for current_number in numbers_list:
    opposite_list.append(-int(current_number))

print(opposite_list)