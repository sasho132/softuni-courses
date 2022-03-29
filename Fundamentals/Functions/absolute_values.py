def get_absolute_value():
    numbers_string = input().split(" ")
    numbers_list = []

    for num in numbers_string:
        number = float(num)
        abs_number = abs(number)
        numbers_list.append(abs_number)

    print(numbers_list)


get_absolute_value()