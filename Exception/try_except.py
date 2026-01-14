"""
Docstring for Exception.try_except
"""


try:
    num = int(input("Enter number: "))
    print("....")
    print(10 / num)
    print("hello")
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Execution completed")
