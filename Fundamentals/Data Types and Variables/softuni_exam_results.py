exam_user_results = {}
submissions = {}

line = input()
while line != "exam finished":
    command = line.split("-")
    if 'banned' in command:
        username = command[0]
        if username in exam_user_results:
            del exam_user_results[username]
    else:
        username = command[0]
        language = command[1]
        points = int(command[2])
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
        if username not in exam_user_results:
            exam_user_results[username] = {language: points}
        else:
            if language not in exam_user_results[username]:
                exam_user_results[username][language] = points
            else:
                if exam_user_results[username][language] < points:
                    exam_user_results[username][language] = points

    line = input()

print("Results:")
for user, language in exam_user_results.items():
    for current_points in language.values():
        print(f"{user} | {current_points}")


print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
