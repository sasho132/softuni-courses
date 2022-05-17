key = int(input())
number = int(input())
message = ""

for i in range(0, number):
    letter = input()
    result = ord(letter) + key
    message += chr(result)

print(message)
