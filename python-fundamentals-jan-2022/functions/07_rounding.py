def round_numbers():
    numbers_string = input().split(" ")
    numbers_list = []

    for num in numbers_string:
        number = float(num)
        round_number = round(number)
        numbers_list.append(round_number)

    print(numbers_list)


round_numbers()