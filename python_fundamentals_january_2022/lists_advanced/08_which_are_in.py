first_strings = input().split(", ")
second_strings = input().split(", ")

filtered = []

for word in first_strings:
    if any(word in x for x in second_strings):
        filtered.append(word)

print(filtered)
