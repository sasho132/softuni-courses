expression = input()

parentheses_stack = list()

for char in range(len(expression)):
    if expression[char] == "(":
        parentheses_stack.append(char)
    elif expression[char] == ")":
        start_index = parentheses_stack.pop()
        print(expression[start_index:char + 1])
