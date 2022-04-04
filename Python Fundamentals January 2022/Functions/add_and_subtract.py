def sum_numbers(first, second):
    return first + second


def subtract(num1, num2):
    return num1 - num2


def add_and_subtract(first, second, third):
    sum_result = sum_numbers(first_number, second_number)
    subtract_result = subtract(sum_result, third_number)
    return subtract_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
