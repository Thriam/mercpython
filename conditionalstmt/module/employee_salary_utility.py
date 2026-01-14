"""
Docstring for mercpython.conditionalstmt.module.employee_salary_utility
"""


def leave_calculator(leaves_taken):
    """
    Docstring for leave_calculator

    :param leaves_taken: Description
    """
    return 0 if leaves_taken <= 15 else leaves_taken - 15


def salary_calculator(role, leaves_taken, day_salary):
    """
    Docstring for salary_calculator

    :param role: Description
    :param leaves_taken: Description
    :param day_salary: Description
    """
    leaves = leave_calculator(leaves_taken)
    match role:
        case "coder":
            days = 30 - leaves
            salary = days * day_salary
            salary = salary * 1.1
            return salary
        case "designer":
            days = 30 - leaves
            salary = days * day_salary
            salary = salary * 1.15
            return salary
        case "manager":
            days = 30 - leaves
            salary = days * day_salary
            salary = salary * 1.05
            return salary
