from collections import deque


bees = deque(int(x) for x in input().split())
nectars_stack = [int(x) for x in input().split()]
symbols = deque(input().split())
total_honey_made = 0

while bees and nectars_stack:
     bee = bees[0]
     nectar = nectars_stack.pop()

     if nectar >= bee:
          bee = bees.popleft()
          operator = symbols.popleft()
     
          if operator == '+':
               total_honey_made += abs(bee + nectar)

          elif operator == '-':
               total_honey_made += abs(bee - nectar)

          elif operator == '*':
               total_honey_made += abs(bee * nectar) 

          elif operator == '/' and nectar > 0:
               total_honey_made += abs(bee / nectar)


print(f"Total honey made: {total_honey_made}")

if bees:
     print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectars_stack:
     print(f"Nectar left: {', '.join(str(x) for x in nectars_stack)}")