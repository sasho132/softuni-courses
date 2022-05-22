students_dict = {}

while True:
    command = input()

    if ":" not in command:
        break

    get_student = command.split(":")
    student_name = get_student[0]
    student_id = int(get_student[1])
    course = get_student[2]

    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][student_id] = student_name


course = " ".join(command.split("_"))
for key, value in students_dict.items():
    if key == course:
        for i, n in value.items():
            print(f"{n} - {i}")
