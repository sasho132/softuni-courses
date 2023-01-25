from collections import deque

chocolates_stack = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolates_stack and cups_of_milk and milkshakes < 5:

    chocolate = chocolates_stack.pop()
    cup = cups_of_milk.popleft()

    if chocolate <= 0 and cup <= 0:
        continue

    if chocolate <= 0:
        cups_of_milk.appendleft(cup)
        continue

    if cup <= 0:
        chocolates_stack.append(chocolate)
        continue

    if chocolate == cup:
        milkshakes += 1
    else:
        cups_of_milk.append(cup)
        chocolates_stack.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates_stack:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates_stack])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(x) for x in cups_of_milk])}")
else:
    print("Milk: empty")
