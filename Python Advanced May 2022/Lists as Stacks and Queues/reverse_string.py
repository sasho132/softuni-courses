text = list(input())

text_stack = list()

for i in range(len(text)):
    text_stack.append(text.pop())

print(''.join(text_stack))
