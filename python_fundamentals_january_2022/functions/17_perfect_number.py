def perfect_number(number_int):
    sum_numbers = 0
    for current_num in range(1, number_int):
        if number_int % current_num == 0:
            sum_numbers += current_num

    if number_int == sum_numbers:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
