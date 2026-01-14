"""
Docstring for mercpython.module.student_grades
"""


def get_student_grade(marks):
    """
    Docstring for get_student_grade

    :param marks: Returns grade from marks
    """
    if marks < 50:
        grade = "fail"
    elif 50 <= marks < 70:
        grade = "merit"
    else:
        grade = "distinction"

    return grade
