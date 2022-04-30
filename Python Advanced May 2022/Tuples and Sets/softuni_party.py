number_of_guests = int(input())
guest_list = set()

for _ in range(number_of_guests):
    guest_list.add(input())

current_guest = input()
while current_guest != "END":
    guest_list.remove(current_guest)
    current_guest = input()

print(len(guest_list))
print('\n'.join(sorted(guest_list)))
