number_of_students = int(input())
students_dict = {}

for _ in range(number_of_students):
    student_name, student_grade = input().split()
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(float(student_grade))

for students in students_dict.items():
    print(f"{students[0]} -> {' '.join([f'{el:.2f}' for el in students[1]])} "
          f"(avg: {(sum(students[1]) / len(students[1])):.2f})")
