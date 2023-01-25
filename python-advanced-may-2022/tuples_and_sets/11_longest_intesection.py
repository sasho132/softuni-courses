n = int(input())
longest_intersection = []

for _ in range(n):
    a, b = input().split('-')
    first_set = set()
    second_set = set()

    first_range_start, first_range_end = a.split(',')
    second_range_start, second_range_end = b.split(',')

    for num1 in range(int(first_range_start), int(first_range_end) + 1):
        first_set.add(num1)
    
    for num2 in range(int(second_range_start), int(second_range_end) + 1):
        second_set.add(num2)

    res = first_set.intersection(second_set)
    if len(res) > len(longest_intersection):
        longest_intersection = list(res)


print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
