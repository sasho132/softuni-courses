text = input()

capital_letters_list = []
for index in range(0, len(text)):
    test_digit = text[index]
    if 65 <= ord(test_digit) <= 90:
        capital_letters_list .append(index)

print(capital_letters_list)
