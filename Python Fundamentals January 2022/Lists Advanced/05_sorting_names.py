names = input().split(", ")

sorted_names = sorted(names, key=lambda word: (-len(word), word))
print(sorted_names)
