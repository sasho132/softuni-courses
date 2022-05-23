import re

text = input()

username = r"(^| )[a-z0-9]+([._-][a-z0-9]+)*"
domain = r"[a-z]+(-[a-z]+)*\.[a-z]+(\.[a-z]+)*"
email_patter = rf"{username}@{domain}"

matches = re.finditer(email_patter, text)
res = []

for match in matches:
    res.append(match.group())

for email in res:
    print(f"{email.strip()}", end="\n")