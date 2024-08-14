def name_inversion(name):
    first, last = name.split(" ", 1)
    return last, " ", first

students = {}
# Get lastname, firstname of high-GPA students
{name_inversion(student.name):student.gpa 
for student in students
if student.gpa > 3.5}