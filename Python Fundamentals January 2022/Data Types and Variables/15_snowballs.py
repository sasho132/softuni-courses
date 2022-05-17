import sys

number_of_snowballs = int(input())
greatest_snowball = -sys.maxsize
greatest_snowball_weight = 0
greatest_snowball_time = 0
greatest_snowball_quality = 0

for snowball in range(0, number_of_snowballs):
    snowball_weight = int(input())
    time_to_target = int(input())
    quality_of_snowball = int(input())
    current_snowball = (snowball_weight / time_to_target) ** quality_of_snowball
    if current_snowball > greatest_snowball:
        greatest_snowball = current_snowball
        greatest_snowball_weight = snowball_weight
        greatest_snowball_time = time_to_target
        greatest_snowball_quality = quality_of_snowball

print(f"{greatest_snowball_weight} : {greatest_snowball_time} = {int(greatest_snowball)} ({greatest_snowball_quality})")
