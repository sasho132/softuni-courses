clothes_stack = list(map(int, input().split()))
rack_capacity = int(input())

racks_counter = 0
current_rack = 0
while clothes_stack:
    if current_rack + clothes_stack[-1] > rack_capacity:
        racks_counter += 1
        current_rack = 0
    else:
        current_rack += clothes_stack.pop()
        if len(clothes_stack) == 1:
            racks_counter += 1

print(racks_counter)
