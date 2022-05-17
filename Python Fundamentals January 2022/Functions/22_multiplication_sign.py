def multiplication_sign(first, second, third):
    res = first * second * third
    if res < 0:
        return "negative"
    elif res == 0:
        return "zero"
    elif res > 0:
        return "positive"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(multiplication_sign(first_number, second_number, third_number))
