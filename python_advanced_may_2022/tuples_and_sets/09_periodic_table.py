n = int(input())
chemical_elements = set()

for _ in range(n):
    chemical_compounds = input().split()
    for el in chemical_compounds:
        chemical_elements.add(el)

print('\n'.join(chemical_elements))
