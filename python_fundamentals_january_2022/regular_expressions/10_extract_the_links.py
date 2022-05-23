import re

valid_links = []

text_data = input()
while text_data:
    pattern = r"\www\.[A-Za-z\d\-]+\.[a-z]+(\.[a-z]+)*"

    matches = re.search(pattern, text_data)
    if matches:
        valid_links.append(matches.group())

    text_data = input()

print('\n'.join(valid_links))