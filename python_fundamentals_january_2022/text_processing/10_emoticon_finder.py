text_data = input()
res = []

for index, char in enumerate(text_data):
    if char == ":" and text_data[index + 1] != " ":
        res.append(text_data[index] + text_data[index + 1])

print('\n'.join(res))
