"""
Purpose: Illustrate basic expresssions and operators in Python.

Author: Bambee Garfield

This file name is:   basic_expressions.py
This module name is: basic_expressions

Expressions

Data analytics is all about getting value out of data.
Expressions are the building blocks of data analytics.

Rather like math expressions, or Excel expressions, Python expressions
are a combination of values, variables, operators, and function calls.

Expressions are made of operands and operators.

- Operators are symbols like +, -, *, /, and =.
- Operands can be values or variables, 
  and can include function calls like len() and str().

Writing expressions in Python is like writing formulas in Excel.

Changes: initial exploration
 
"""

from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)

# Declare some variables 
# TODO: Try changing the values of these variables
# TODO: Add some new variables and calculate the area of a rectangle ()
triangle_base = 8
triangle_height = 3
i = 40
j = 10
a = 1.5
b = 2.5
c = 3.6

# Try some operators (multiply, divide, add, subtract)
triangle_area = triangle_base * triangle_height / 2
sum = c + b
difference = b - j

# Log some information using f-strings (formatted strings)
logger.info(f"Given base={triangle_base} and height={triangle_height}, the triangle area = {triangle_area}")
logger.info(f"Given a={a} and b={b}, the sum = {sum}")
logger.info(f"Given i={i} and j={j}, the difference = {difference}")


# Use built-in open() function to read the log file and print it to the terminal
with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())
