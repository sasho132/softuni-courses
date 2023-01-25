def sum_numbers(numbers):
    positive_numbers_sum = sum([x for x in numbers if x > 0])
    negative_numbers_sum = sum([x for x in numbers if x < 0])

    return positive_numbers_sum, negative_numbers_sum


nums = [int(x) for x in input().split()]
print(sum_numbers(nums)[1])
print(sum_numbers(nums)[0])
if abs(sum_numbers(nums)[1]) > sum_numbers(nums)[0]:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
