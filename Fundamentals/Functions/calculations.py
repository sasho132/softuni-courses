def operations_solve(operator, a, b):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b


input_operator = input()
num1 = int(input())
num2 = int(input())

result = operations_solve(input_operator, num1, num2)
print(result)