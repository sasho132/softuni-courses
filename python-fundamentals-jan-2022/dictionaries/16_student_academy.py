num = int(input())
students_dict = {}

for s in range(num):
    student = input()
    grade = float(input())

    if student not in students_dict:
        students_dict[student] = []
    students_dict[student].append(grade)

for key, value in students_dict.items():
    if (sum(students_dict[key]) / len(students_dict[key])) >= 4.50:
        print(f"{key} -> {sum(students_dict[key]) / len(students_dict[key]):.2f}")
