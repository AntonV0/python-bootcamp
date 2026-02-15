"""Python Fundamentals & Exception Handling – Summary Guide"""

# ======================================================
# 1. VARIABLES IN PYTHON
# ======================================================

# A variable in Python is a *reference name* that points to an object in memory.
# In Python, EVERYTHING is an object (numbers, strings, lists, functions, etc).

# Example:
import keyword
a = 89
print(a)
print(type(a))  # <class 'int'>

# ------------------------------------------------------
# Variable Naming Rules
# ------------------------------------------------------
# - Must start with a letter (a–z, A–Z) or underscore (_)
# - Can contain letters, numbers, and underscores
# - Cannot start with a number
# - No spaces allowed
# - No special characters (!@#$%^&*)
# - Case-sensitive
# - Keywords are NOT allowed as variable names

# ------------------------------------------------------
# Naming Conventions
# ------------------------------------------------------
# camelCase     -> myVariable
# snake_case    -> my_variable   (preferred in Python)
# PascalCase    -> MyVariable
# UPPERCASE     -> CONSTANT_NAME

# ======================================================
# 2. ASSIGNING VARIABLES
# ======================================================

# Single assignment
a = 7
b = 6

# Multiple assignment
a = b = c = 7

# Tuple assignment (unpacking)
x, y = 8, 9

# Packing
values = 8, 9, 10, 9.89  # tuple
print(values)

# Unpacking
a, b = values[:2]

# ======================================================
# 3. EVERYTHING IS AN OBJECT
# ======================================================

# Integers are objects with methods
num = 78
print(num.bit_length())
print(type(num))

# Operators are actually method calls
a = 5
b = 3
print(a + b)
print(a.__add__(b))

# Lists are mutable objects
items = [1, 2, 3]
items.append("cars")

# ======================================================
# 4. STATIC vs DYNAMIC TYPING
# ======================================================

# Static typing (C, Java)
# int a = 10;

# Dynamic typing (Python)
a = 10
a = "hello"

# ======================================================
# 5. KEYWORDS
# ======================================================

# Keywords are reserved words with special meaning
# Examples: if, else, for, while, try, except, raise, True, False, None

print(keyword.kwlist)

# ======================================================
# 6. EXCEPTION HANDLING – WHY IT EXISTS
# ======================================================

# Without exception handling:
# - Program crashes
# - No user-friendly message
# - No cleanup

# Exception handling allows us to:
# - Prevent crashes
# - Handle invalid user input
# - Show helpful error messages
# - Keep the program running

# ======================================================
# 7. TRY / EXCEPT / ELSE / FINALLY
# ======================================================

# try     -> code that may fail
# except  -> handles specific errors
# else    -> runs if no error occurred
# finally -> always runs (cleanup)

# Example:
try:
    a = 10
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Execution completed")

# ======================================================
# 8. COMMON EXCEPTIONS YOU CAN HANDLE
# ======================================================

# - ZeroDivisionError
# - ValueError
# - TypeError
# - IndexError
# - KeyError
# - FileNotFoundError

# Example:
try:
    x = int("ten")
except ValueError:
    print("Invalid number")

# ======================================================
# 9. AVOID BARE except:
# ======================================================

# BAD:
try:
    x = int("abc")
except:
    print("Something went wrong")

# GOOD:
try:
    x = int("abc")
except ValueError as e:
    print(e)

# ======================================================
# 10. RAISING CUSTOM EXCEPTIONS
# ======================================================

try:
    age = int(input("Enter age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above")
    print("Eligible to vote")
except ValueError as e:
    print(e)

# ======================================================
# 11. NESTED TRY / EXCEPT
# ======================================================

try:
    a = int(input("Enter a number: "))
    try:
        b = int(input("Enter another number: "))
        print(a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero")
except ValueError:
    print("Invalid input")

# ======================================================
# 12. OPERATORS OVERVIEW
# ======================================================

# Arithmetic: +, -, *, /, //, %, **
# Logical: and, or, not
# Comparison: ==, !=, <, >, <=, >=
# Assignment: =, +=, -=, *=, /=
# Identity: is, is not
# Membership: in, not in

# Floor division
print(1234567 // 13)

# Power operator
print(2 ** 4)
