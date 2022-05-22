def letters_sum(some_string, count_chars):
    current_result = 0
    for char in some_string[- exclusive_letters:]:
        current_result += ord(char)
    return current_result


text = input().split()
res = 0
string1 = text[0]
string2 = text[1]

for x, y in zip(text[0], text[1]):
    res += ord(x) * ord(y)

if len(string1) > len(string2):
    exclusive_letters = len(string1) - len(string2)
    res += letters_sum(string1, exclusive_letters)

elif len(string1) < len(string2):
    exclusive_letters = len(string2) - len(string1)
    res += letters_sum(string2, exclusive_letters)

print(res)
