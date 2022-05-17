start_char = int(input())
end_char = int(input())

for char in range(start_char, end_char + 1):
    number_in_char = chr(char)
    print(f"{number_in_char}", end=" ")
    