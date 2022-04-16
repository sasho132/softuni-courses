def get_sum_even_and_odd_digits(number):
    even_sum = 0
    odd_sum = 0

    for num in range(len(number)):
        if int(number[num]) % 2 == 0:
            even_sum += int(number[num])
        else:
            odd_sum += int(number[num])

    return odd_sum, even_sum


single_number = input()
sum_of_odd_numbers, sum_of_even_numbers = get_sum_even_and_odd_digits(single_number)
print(f"Odd sum = {sum_of_odd_numbers}, Even sum = {sum_of_even_numbers}")
