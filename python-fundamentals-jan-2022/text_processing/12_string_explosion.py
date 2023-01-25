string_data = input()

data = [x for x in string_data]
strength_left = 0

for index, char in enumerate(data):
    if data[index - 1] == ">":
        explosion_value = int(char) + strength_left
        for i in range(explosion_value):
            if data[index] == ">":
                strength_left = explosion_value - i
                break
            else:
                data[index] = ""
            if index + 1 < len(data):
                index += 1
            else:
                break

print(''.join(data))
