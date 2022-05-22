number = int(input())
word = input()
strings_list = []
filtered_strings = []

for strings in range(number):
    current_strings = input()
    strings_list.append(current_strings)
    if word in current_strings:
        filtered_strings.append(current_strings)

print(strings_list)
print(filtered_strings)
