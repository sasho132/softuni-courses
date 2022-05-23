import re

nums = []

line = input()
while line:
    matches = re.finditer(r'([0-9]+)', line)
    for match in matches:
        nums.append(match.group(1))

    line = input()

print(' '.join(nums))