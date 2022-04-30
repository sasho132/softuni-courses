n = int(input())
usernames = set()  

for i in range(n):
    usernames.add(input())

print('\n'.join(usernames))
