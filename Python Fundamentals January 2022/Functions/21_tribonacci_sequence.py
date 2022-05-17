def tribonacci_sequence(number):
    numbers_list = []
    string_list = []
    for num in range(number):
        numbers_list.append(1)

    for index, digit in enumerate(numbers_list):
        if index == 0 or index == 1:
            continue
        elif index == 2:
            numbers_list[index] = 2
            continue
        elif index > 2:
            numbers_list[index] = numbers_list[index - 1] + numbers_list[index - 2]\
                                  + numbers_list[index - 3]
            continue

    for digit in numbers_list:
        string_list.append(str(digit))

    return ' '.join(string_list)


integer_number = int(input())
print(tribonacci_sequence(integer_number))
