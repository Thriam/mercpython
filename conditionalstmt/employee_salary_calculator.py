"""
Docstring for mercpython.conditionalstmt.employee_salary_calculator
"""


import logging


from module.employee_salary_utility import salary_calculator

logging.basicConfig(level=logging.INFO)
logging.info("Program Started")
logging.warning("Maintain case senstivity")
print(salary_calculator(input("Role (coder or designer or manager): "),
                        int(input("Leaves Taken: ")),
                        int(input("Day Salary: "))))
logging.info("Program Ended")
