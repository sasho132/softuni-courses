text_data = input()
text_list = [x for x in text_data]

for index, char in enumerate(text_list):
    if index + 1 >= len(text_list):
        break
    if text_list[index + 1] == char:
        text_list[index] = ""

print(''.join(text_list))
