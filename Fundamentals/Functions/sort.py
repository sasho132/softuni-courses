numbers = input().split(" ")

integers_list = []
for num in numbers:
    integers_list.append(int(num))

sorted_list = sorted(integers_list)
print(sorted_list)
