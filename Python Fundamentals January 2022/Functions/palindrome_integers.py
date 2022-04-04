def check_for_palindrome(numbers):
    numbers_list = numbers.split(", ")
    palindrome_list = []

    for number in numbers_list:
        current_number = ""
        for num in range(len(number) - 1, - 1, - 1):
            current_number += number[num]

        if current_number == number:
            palindrome_list.append("True")
        else:
            palindrome_list.append("False")

    return palindrome_list


integer_numbers = input()
res = check_for_palindrome(integer_numbers)

for palindrome in res:
    print(palindrome)
