def get_factorial(num1, num2):
    for first_integer in range(1, num1):
        num1 *= first_integer
    for second_integer in range(1, num2):
        num2 *= second_integer
    return f"{num1 / num2:.2f}"


first_number = int(input())
second_number = int(input())
print(get_factorial(first_number, second_number))
