courses_dict = {}

input_line = input()
while input_line != "end":
    course_name, student_name = input_line.split(" : ")
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)

    input_line = input()

for key, value in courses_dict.items():
    print(f"{key}: {len(value)}")
    for student in courses_dict[key]:
        print(f"-- {student}")
