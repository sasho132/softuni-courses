numbers = input().split(", ")

positive_filter = [int(x) for x in numbers if int(x) >= 0]
negative_filter = [int(x) for x in numbers if int(x) < 0]
even_filter = [int(x) for x in numbers if int(x) % 2 == 0]
odd_filter = [int(x) for x in numbers if int(x) % 2 != 0]

positive = ", ".join([str(x) for x in positive_filter])
negative = ", ".join([str(x) for x in negative_filter])
even = ", ".join([str(x) for x in even_filter])
odd = ", ".join([str(x) for x in odd_filter])

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Even: {even}")
print(f"Odd: {odd}")
