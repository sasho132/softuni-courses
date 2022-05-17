# Convert lowercase in uppercase in input()
data = input().upper()

res = ""
current_string = ""
current_number = ""

for index, char in enumerate(data):
    if char.isnumeric():
        current_number += char
        if index + 1 < len(data) and data[index + 1].isnumeric():
            current_number += data[index + 1]
        res += int(current_number) * current_string
        current_string = ""
        current_number = ""
    else:
        current_string += char

# Get len() from unique symbols in res
symbol_counter = len(set([x for x in res]))

print(f"Unique symbols used: {symbol_counter}")
print(res)
