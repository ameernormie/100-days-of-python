student_list = []


def add_student(name, id=0):
    """
    Adds a student in the student list
    :param name: string - student-name
    :param id:   int - student id
    """
    student = {"name": name, "student_id": id}
    student_list.append(student)


add_student('Ameer', 23)

# Python also supports named arguments
add_student(id=45, name="Hamza")

print(student_list)


# Variable number of arguments in function


def var_args(name, *args):
    print(name)
    print(args)


var_args('Ameer', "loves python", True)


# Keyword arguments


def keyword_args(name, **kwargs):
    print(name)
    print(kwargs["description"])


keyword_args('Ameer', description="loves python", does_he=True)
