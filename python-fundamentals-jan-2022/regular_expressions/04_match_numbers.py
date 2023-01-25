import re

text = input()

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"
matches = re.finditer(pattern, text)

res = []

for match in matches:
    res.append(match.group())

print(' '.join(res))