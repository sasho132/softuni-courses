first = set([int(x) for x in input().split()])
second = set([int(x) for x in input().split()])

n = int(input())

for _ in range(n):
    line = input().split()
    
    command = line[0]
    subcommand = line[1]

    if command == 'Add':
        if subcommand == 'First':
            [first.add(int(x)) for x in line[2:]]
        elif subcommand == 'Second':
            [second.add(int(x)) for x in line[2:]]
    
    elif command == 'Remove':
        if subcommand == 'First':
            first = first.difference([int(x) for x in line[2:]])
        elif subcommand == 'Second':
            second = second.difference([int(x) for x in line[2:]])
    
    else:
        print(first.issubset(second) or second.issubset(first))

print(', '.join([str(x) for x in sorted(first)]))
print(', '.join([str(x) for x in sorted(second)]))
