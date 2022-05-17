import string


def username_validator(usernames):
    valid_elements = string.digits + string.ascii_letters + "-" + "_"

    for usr_name in usernames:
        if 3 <= len(usr_name) <= 16:
            valid_condition = True
            for index, letter in enumerate(usr_name):
                if letter not in valid_elements:
                    valid_condition = False
                    break
            if valid_condition:
                print(usr_name)


usernames_data = input().split(", ")

username_validator(usernames_data)
