from collections import deque

data_stack = list()
num = int(input())

for n in range(num):
    current_queue = deque(input().split(" "))
    command_num = current_queue.popleft()
    if command_num == '1':
        current_number = current_queue.pop()
        data_stack.append(current_number)
    elif command_num == '2' and data_stack:
        data_stack.pop()
    elif command_num == '3' and data_stack:
        print(max(data_stack))
    elif command_num == '4' and data_stack:
        print(min(data_stack))

while len(data_stack) > 1:
    print(data_stack.pop(), end=', ')
else:
    print(data_stack.pop())
