nums = input().split(' ')
reversed_stack = list()

for n in range(len(nums)):
    reversed_stack.append(nums.pop())

print(' '.join(reversed_stack))
