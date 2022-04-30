num = int(input())
unique_names = set()

for _ in range(num):
    unique_names.add(input())
    
for name in unique_names:
    print(name)

