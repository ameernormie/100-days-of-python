students = []


def get_students_title_case():
    student_title_case = []
    for student in students:
        student_title_case.append(student['name'].title())
    return student_title_case


def print_student_titlecase():
    students_titlecase = get_students_title_case()
    print(students_titlecase)


def add_student(name, student_id=0):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open('students.txt', "a")
        f.write(student + '\n')
        f.close()
    except Exception:
        print('Could not save file')


def read_file():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print('Could not read file')


read_file()
print_student_titlecase()


while True:                                 # Keep asking user unless he/she says no
    student_name = input('Enter name: ')
    student_id = input('Enter id: ')

    add_student(student_name, student_id)
    save_file(student_name)

    add_another_student = input(
        'Do you want to add another student? y/n Y/N :')

    if add_another_student == 'n' or add_another_student == 'N':
        break


# print_student_titlecase()
