def math_operations(*args, **kwargs):
    operations_dict = kwargs

    for num in range(len(args)):
        if num % 4 == 0:
            operations_dict['a'] += args[num]
        elif num % 4 == 1:
            operations_dict['s'] -= args[num]
        elif num % 4 == 2 and args[num] != 0:
            operations_dict['d'] /= args[num]
        elif num % 4 == 3:
            operations_dict['m'] *= args[num]

    sorted_operation_dict = sorted(operations_dict.items(), key=lambda kv: (-kv[1], kv[0]))
    result = ''
    for key, value in sorted_operation_dict:
        result += f"{key}: {value:.1f}\n"
    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))