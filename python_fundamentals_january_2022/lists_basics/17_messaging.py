numbers = input().split(" ")
text = input()
integers_list = []
message = ""

for number in numbers:
    current_sum = 0
    for index, num in enumerate(number):
        current_sum += int(num)
    integers_list.append(current_sum)
    char = current_sum % len(text)
    message += text[char]
    if len(text) > char:
        text = text[0:char:] + text[char + 1::]

current_sum = 0
print(message)