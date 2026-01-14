"""
Docstring for mercpython.conditionalstmt.employee_salary_calculator
"""


from module.employee_salary_utility import salary_calculator

print(salary_calculator(input("Role: "),
                        int(input("Leaves Taken: ")),
                        int(input("Day Salary: "))))
