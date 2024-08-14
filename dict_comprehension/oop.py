class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major

# given a list of student objects, write a
# dictionary comprehension mapping students
# to gpa.

#________DICT_COMPREHENSION_________#
# {key:value for VAR in SEQ}
students = {}
{student.name:student.gpa for student in students}


# A list of student majors
[student.majors for student in students]

# A set of students' majors
{student.majors for student in students}

cs_students = (
    student.gpa
    for student in students
    if student.major == "CSC"
    )

