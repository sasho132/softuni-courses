beggars_sums = input().split(", ")
count_of_beggars = int(input())
beggars_sum_integers = []
taken_beggars_sums = []
current_beggar_sum = 0
beggar_counter = 0

for number in beggars_sums:
    beggars_sum_integers.append(number)

for beggar in range(count_of_beggars):
    for current_sum in range(beggar_counter, len(beggars_sum_integers), count_of_beggars):
        current_beggar_sum += int(beggars_sum_integers[current_sum])
    beggar_counter += 1
    taken_beggars_sums.append(current_beggar_sum)
    current_beggar_sum = 0

print(taken_beggars_sums)
