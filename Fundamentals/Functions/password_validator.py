def valid_password_len(password):
    if 6 <= len(password) <= 10:
        return True
    return False


def valid_symbols(text):
    res = text.isalnum()
    return res


def valid_digits(string):
    digits_counter = 0
    for digit in string:
        if digit.isdigit():
            digits_counter += 1
    if digits_counter >= 2:
        return True
    return False


password_text = input()
if valid_password_len(password_text) and valid_symbols(password_text) and\
        valid_digits(password_text):
    print("Password is valid")
else:
    if not valid_password_len(password_text):
        print("Password must be between 6 and 10 characters")
    if not valid_symbols(password_text):
        print("Password must consist only of letters and digits")
    if not valid_digits(password_text):
        print("Password must have at least 2 digits")
