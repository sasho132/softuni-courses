import sys

divisor = int(input())
boundary = int(input())
2
largest_number_found = -sys.maxsize

for number in range(1, boundary + 1):
    if number % divisor == 0:
        if number > largest_number_found:
            largest_number_found = number

print(largest_number_found)
