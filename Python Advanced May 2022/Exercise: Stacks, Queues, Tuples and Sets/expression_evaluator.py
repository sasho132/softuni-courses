from collections import deque


data = input().split()

numbers = deque()

for ch in data:
    if ch in '+-*/':
        if ch == '+':
            while len(numbers) > 1:
                first = numbers.popleft()
                second = numbers.popleft()
                numbers.appendleft(first + second)

        elif ch == '-':
            while len(numbers) > 1:
                first = numbers.popleft()
                second = numbers.popleft()
                numbers.appendleft(first - second)

        elif ch == '*':
            while len(numbers) > 1:
                first = numbers.popleft()
                second = numbers.popleft()
                numbers.appendleft(first * second)

        elif ch == '/':
            while len(numbers) > 1:
                first = numbers.popleft()
                second = numbers.popleft()
                numbers.appendleft(first // second)
    
    else:
        numbers.append(int(ch))

print(numbers.popleft())
