import re

names = input()

pattern = r"\+359([ -])2\1\d{3}\1\d{4}\b"
matches = re.finditer(pattern, names)

res = []
for match in matches:
    res.append(match.group())

print(', '.join(res))