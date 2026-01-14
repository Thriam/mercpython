"""
Docstring for mercpython.conditionalstmt.employee_salary_calculator
"""


from module.employee_salary_utility import salary_calculator

print(salary_calculator(input("Role: "),
                        input("Leaves Taken: "),
                        input("Day Salary: ")))
