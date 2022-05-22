parenthesis = list(input())
opening_brackets = []
balanced_parenthesis = True

for ch in parenthesis:
    if ch in '{, (, [':
        opening_brackets.append(ch)
    else:
        if not opening_brackets:
            balanced_parenthesis = False
            break
        else:
            if opening_brackets.pop() + ch not in '{}()[]':
                balanced_parenthesis = False
                break

if balanced_parenthesis:
    print('YES')
else:
    print('NO')
