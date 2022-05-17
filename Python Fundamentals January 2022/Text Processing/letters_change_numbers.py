import string


def first_letter(letters):
    upper_cases = string.ascii_uppercase
    lower_cases = string.ascii_lowercase
    digits = string.digits

    res = 0
    current_digits = ''.join([x for x in letters if x in digits])

    if letters[0] in upper_cases:
        index = upper_cases.index(letters[0])
        res += int(current_digits) / (index + 1)

    elif letters[0] in lower_cases:
        index = lower_cases.index(letters[0])
        res += int(current_digits) * (index + 1)

    if letters[-1] in upper_cases:
        index = upper_cases.index(letters[-1])
        res -= (index + 1)

    elif letters[-1] in lower_cases:
        index = lower_cases.index(letters[-1])
        res += (index + 1)

    return res


letters_data = input().split()
total = 0

for current_string in letters_data:
    total += first_letter(current_string)

print(f"{total:.2f}")
