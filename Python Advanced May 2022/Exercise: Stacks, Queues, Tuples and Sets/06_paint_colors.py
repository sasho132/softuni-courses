from collections import deque

string_list = deque(input().split())
colors = ['red', 'yellow', 'blue']
subcolors = ['orange', 'purple', 'green']
saved_colors = []

while string_list:
    first_substring = string_list.popleft()
    if string_list:
        second_substring = string_list.pop()
    else:
        second_substring = ''

    result = first_substring + second_substring
    if result in colors or result in subcolors:
        if result not in saved_colors:
            saved_colors.append(result)
            continue

    result = second_substring + first_substring
    if result in colors or result in subcolors:
        if result not in saved_colors:
            saved_colors.append(result)
            continue

    string_middle = len(string_list) // 2
    first_substring = first_substring[:-1]
    second_substring = second_substring[:-1]
    if first_substring:
        string_list.insert(string_middle, first_substring)
    if second_substring:
        string_list.insert(string_middle, second_substring)

result_colors = []
for current_color in saved_colors:
    if current_color in colors:
        result_colors.append(current_color)
    elif current_color == 'orange':
        if 'red' in saved_colors and 'yellow' in saved_colors:
            result_colors.append(current_color)
    elif current_color == 'purple':
        if 'red' in saved_colors and 'blue' in saved_colors:
            result_colors.append(current_color)
    elif current_color == 'green':
        if 'yellow' in saved_colors and 'blue' in saved_colors:
            result_colors.append(current_color)

print(result_colors)
