students = []


class Student:

    # Class attribute available to all instances
    school_name = "Afzal Public School"

    def __init__(self, name, student_id=0):            # 2nd argument is optional
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return 'Student ' + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):
    school_name = "F.G Sir Syed Collge"

    def get_school_name(self):
        return self.school_name

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + 'HS'
