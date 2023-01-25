def data_type_function(first, second):
    if first == "string":
        return f"${second}$"
    elif first == "int":
        return int(second) * 2
    elif first == "real":
        return f"{float(second) * 1.5:.2f}"


first_string = input()
second_string = input()
print(data_type_function(first_string, second_string))
