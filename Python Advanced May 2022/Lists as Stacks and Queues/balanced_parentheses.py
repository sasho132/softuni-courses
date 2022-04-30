parenthesis = list(input())
opening_brackets = []
balanced_paranthesis = True

for ch in parenthesis:
    if ch in '{, (, [':
        opening_brackets.append(ch)
    else:
        if not opening_brackets:
            balanced_paranthesis = False
            break
        else:
            if opening_brackets.pop() + ch not in '{}()[]':
                balanced_paranthesis = False
                break

if balanced_paranthesis:
    print('YES')
else:
    print('NO')
