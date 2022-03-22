contest_dict = {}
submissions = {}

line = input()
while line != 'end of contests':
    line_split = line.split(':')
    contest = line_split[0]
    password = line_split[1]
    contest_dict[contest] = password

    line = input()

command = input()
while command != 'end of submissions':
    command_split = command.split('=>')
    current_contest = command_split[0]
    current_password = command_split[1]
    username = command_split[2]
    user_points = int(command_split[3])

    if current_contest in contest_dict:
        if current_password == contest_dict[current_contest]:
            if username not in submissions:
                submissions[username] = {current_contest: user_points}
            else:
                if current_contest in submissions[username]:
                    if submissions[username][current_contest] < user_points:
                        submissions[username][current_contest] = user_points
                else:
                    submissions[username][current_contest] = user_points

    command = input()

best_candidate = ''
best_points = 0
for user in submissions:
    total_points = sum(submissions[user].values())
    if total_points > best_points:
        best_points = total_points
        best_candidate = user

print(f"Best candidate is {best_candidate} with total {best_points} points.")
print('Ranking:')

for user, user_submissions in sorted(submissions.items()):
    print(f"{user}")
    for key, value in sorted(user_submissions.items(), key=lambda kvpt: -kvpt[1]):
        print(f"#  {key} -> {value}")
