version = input().split(".")
first_number = int(version[0])
second_number = int(version[1])
third_number = int(version[2])

third_number += 1
if third_number > 9:
    third_number = 0
if third_number == 0:
    second_number += 1
    if second_number > 9:
        second_number = 0
        first_number += 1

print(f"{first_number}.{second_number}.{third_number}")
