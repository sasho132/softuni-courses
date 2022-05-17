text = input()

res = [(chr(ord(x) + 3)) for x in text]

print(''.join(res))
