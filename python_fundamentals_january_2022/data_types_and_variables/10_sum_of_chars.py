number_of_lines = int(input())
total_sum = 0

for line in range(number_of_lines):
    current_letter = input()
    current_letter_in_number = ord(current_letter)
    total_sum += current_letter_in_number

print(f"The sum equals: {total_sum}")
