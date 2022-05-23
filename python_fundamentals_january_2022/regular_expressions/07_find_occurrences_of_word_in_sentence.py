import re

text = input()
matches = re.findall(rf'\b{input()}\b', text, re.IGNORECASE)

print(len(matches))