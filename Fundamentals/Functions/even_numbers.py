def filter_even_numbers(numbers):
    even_number_list = []

    for num in range(len(numbers)):
        if int(numbers[num]) % 2 == 0:
            even_number_list.append(int(numbers[num]))

    return even_number_list


sequence_of_numbers = input().split(" ")
res = filter_even_numbers(sequence_of_numbers)
print(res)
