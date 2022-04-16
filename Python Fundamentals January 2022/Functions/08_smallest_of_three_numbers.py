def get_smallest_number(first_number, second_number, third_number):
    numbers_list = [first_number, second_number, third_number]
    smallest_number = min(numbers_list)
    return smallest_number


num1 = int(input())
num2 = int(input())
num3 = int(input())

smallest_number = get_smallest_number(num1, num2, num3)
print(smallest_number)
