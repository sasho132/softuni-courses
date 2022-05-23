import re

furniture = []
total_cost = 0

line = input()
while line != "Purchase":
    pattern = r'>>(?P<name>\w+)<<(?P<price>[0-9]+(\.[0-9]+)*)!(?P<quantity>[0-9]+)'
    line_data = re.finditer(pattern, line)
    for match in line_data:
        if match.group('name') and match.group('price') and match.group('quantity'):
            furniture_name = match.group('name')
            price = float(match.group('price'))
            quantity = int(match.group('quantity'))
            furniture.append(furniture_name)
            total_cost += price * quantity
    line = input()

print("Bought furniture:")
if len(furniture) > 0:
    print('\n'.join(furniture))
print(f"Total money spend: {total_cost:.2f}")