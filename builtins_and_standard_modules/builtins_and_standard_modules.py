"""Built-ins and Standard Modules"""

# Before you write an import statement, you have access to the builtins module.
# This module contains essential functions like print(), len(), int(), input(), range(), and type()
# Also includes built-in exception types like ValueError, TypeError, and IndexError.

import sys  # sys module provides access to system-specific parameters and functions
import math  # math module provides mathematical functions and constants
import random  # random module provides functions for generating random numbers

# Importing the user-defined module
import package.pack_1.module_1  # Importing module_1 from package
import package.pack_2.module_2  # Importing module_2 from package
import user_defined_module as user_defined_module


l1 = [1, 34, 100, 32, -6, 5/89]
l1.sort()  # Sorts the original list in place, returns None, only works on lists
print(l1)  # Returns a new sorted list
print(sorted(l1))  # Returns a new sorted list, does not modify the original list
# sorted() works on any iterable, not just lists (tuples, strings, etc.)

t1 = (90, 98, 67, -5, 2.78)
ans = sorted(t1)  # Works on tuples too
print(tuple(ans))  # Convert back to tuple if needed

# t1.sort()  # This will raise an AttributeError since tuples don't have a sort() method
print(t1)  # Original tuple remains unchanged

# ======================================================

# Builtins:

# These are functions, types, classes and constants, automatically available without imports.
# Examples: abs(), all(), any(), bool(), dict(), float(), int(), list(), len(),
# max(), min(), print(), str(), sum(), type(), zip()
# ValueError, TypeError, IndexError are built-in exceptions
# int, None, list, str are built-in types

print(dir(__builtins__))  # Lists all built-in functions, types, and exceptions
# Double underscore before and after builtins indicates it's a special Python object
# __builtins__ is a special Python object that contains all built-in functions, types, & exceptions
# __builtins__ --> name
# Points to --> internal object
# Object contains --> references to built-ins

# Objects --> the real data stored in memory
# print reference --> print() function
# len reference --> len() function

# For example:
name = input("Enter name: ")  # input() is a built-in function
print("Hello,", name)

l2 = [1, 100, 67, 91, -7, 9.56]
# print(l1.max()) This will raise an AttributeError since lists don't have a max() method
print(max(l2))  # Correct way to use built-in max() function

l3 = ["hello", "p", "g", 89, 100, -6, 0.89]
# print(max(l3))  # TypeError: '>' not supported between instances of 'int' and 'str'

a = 8
# Using the "dunder" method form of addition without using + operator
print(a.__add__(4))

# ======================================================

# Standard Modules:
# These are modules that come pre-installed with Python.
# These are python files with code, with .py extension, stored in the standard library.
# You can import and use them in your programs.
# Examples: math, random, datetime, os, sys, json, re, collections, itertools

# import sys (top of the file)
# Lists all built-in modules available in the Python interpreter
print(sys.builtin_module_names)
print(sys.version)  # Displays the Python version information

# ======================================================

# Using the math module:
# import math (top of the file)
print(dir(math))  # Lists all functions and constants in the math module

print(math.sqrt(64))  # Using sqrt() function from math module (8.0)
print(math.pi)  # Using pi constant from math module (3.141592653589793)
print(math.factorial(7))  # Using factorial() function from math module (5040)
print(math.ceil(4.678))  # Rounds up to the nearest integer (5)
print(math.floor(4.678))  # Rounds down to the nearest integer (4)
print(math.log10(1000))  # Base-10 logarithm (3.0)

# Calculating area of a circle
radius = 5
area = math.pi * math.pow(radius, 2)  # Area = πr²
# Alternatively: area = math.pi * radius ** 2
print("Area of circle with radius", radius, "is %f" % area)
# %f formats the floating-point number, % area inserts the area value
# Output: Area of circle with radius 5 is 78.53981633974483
print("Area of circle with radius", radius, "is %.3f" % area)
# Output: Area of circle with radius 5 is 78.540

# Alternative way using str.format()
print("Value is {:.2f}".format(area))  # Output: Value is 78.54

name = "Anton"
print("My name is %s" % name)  # Output: My name is Anton
# %s formats the string, % name inserts the name value

age = 31
place = "England"
print("My name is", name, ". I am", age, "years old and I live in", place, ".")
# My name is Anton . I am 31 years old and I live in England .
# The commas automatically add spaces between items

print("My name is {}. I am {} years old and I live in {}.".format(name, age, place))
# My name is Anton. I am 31 years old and I live in England.

# ======================================================

# Using the random module:
# import random (top of the file)
print(dir(random))  # Lists all functions and constants in the random module

print(random.random())  # Random float between 0.0 and 1.0
print(random.randint(1, 100))  # Random integer between 1 and 100 (inclusive)

students = ["A", "B", "C", "D", "E"]
print(random.choice(students))  # Randomly selects one element from the list

cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards)  # Shuffles the list in place
print(cards)  # Prints the shuffled list

names = ["Alice", "Bob", "Charlie", "David"]
winner = random.choice(names)  # Randomly selects a winner
print("The right answer is:", winner)

n = input("Guess the name: ")
if n == winner:
    print("You guessed it right!")
else:
    print("Wrong guess.")

# ======================================================

# User-defined Modules:
# You can create your own modules by writing Python code in .py files.
# user_defined_module.py is created in the same directory as this file.

# Method 1: Import the entire module
# Accessing variable 'a' from user_defined_module.py
print(user_defined_module.a)
# Output: Python is the most user friendly language
print(user_defined_module.l1)
# Output: ['Anton', 'Ben', 'Catherine', 'Diana', 40, 25.5]

# Print strings from list l1 in user_defined_module
for name in user_defined_module.l1:
    if isinstance(name, str):  # isinstance() checks if the variable is of type str
        print(name)
# Output:
# Anton
# Ben
# Catherine
# Diana

# Method 2: Import specific variables or functions from the module
# from user_defined_module import a, l1 (should be at the top of the file)

# Method 3: The * means import everything from the module
# (not recommended as it can overwrite existing variables)
# from user_defined_module import * (should be at the top of the file)

# Method 4: Import with an alias (using "as" keyword)
# import user_defined_module as udm (should be at the top of the file)

# ======================================================

# Importing user-defined packages:

# A package is a collection of modules in directories that give a package hierarchy.
# A package must contain a special file called __init__.py (can be empty).
# You can create your own packages by creating folders with __init__.py files.
# To use a package, you can import it like a module.

# In this directory, there is a "package" folder with 2 folders: "pack_1" and "pack_2".
# Each folder contains an __init__.py file and a module ("module_1.py" or "module_2.py")).

# import package.pack_1.module_1  # Importing module_1 from package (top of the file)
# import package.pack_2.module_2  # Importing module_2 from package (top of the file)

# Accessing variable from module_1
print(package.pack_1.module_1.alphabet_vowels)
# Output: ['a', 'e', 'i', 'o', 'u']

# Accessing variable from module_2
print(package.pack_2.module_2.alphabet_consonants)
# Output: ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's',
#          't', 'v', 'w', 'x', 'y', 'z']

# Method 2: Import specific variables from the module
# from package.pack_1.module_1 import alphabet_vowels
# from package.pack_2.module_2 import alphabet_consonants
# Accessing variables directly:
# print(alphabet_vowels)
# print(alphabet_consonants)

# Method 3: Import with an alias
# import package.pack_1.module_1 as mod1
# import package.pack_2.module_2 as mod2
# Accessing variables using aliases:
# print(mod1.alphabet_vowels)
# print(mod2.alphabet_consonants)

# ======================================================

# Side note on functions:

# A function is a reusable block of code that performs a specific task.
# Instead of repeating the same code many times, we define it once and call it whenever we need it.

# Example without a function (repetition):
print("Greetings user!!!")
print("Greetings user!!!")
print("Greetings user!!!")

# This is repetitive and hard to maintain.

# Defining a function using 'def'
# Syntax:
# def function_name():
#     statements
#     statements


def greeting():
    print("Greetings user!!!")


# Calling the function
greeting()

# Using a loop to call the function multiple times
for _ in range(3):  # Using _ as a throwaway variable
    greeting()

# ======================================================

# Example 2 – Function with internal variables


def profile():
    name = "Anton"
    age = 31
    print("My name is", name, "and my age is", age)


profile()  # Preferred way to call the function
# Output: My name is Anton and my age is 31

# Functions are also objects in Python
# You can assign them to variables
d1 = profile
d1()  # Calls the same function
# Output: My name is Anton and my age is 31

# ======================================================

# Function with parameters (inputs)


def greet_user(user_name):
    print("Hello,", user_name)


greet_user("Anton")  # Output: Hello, Anton
greet_user("Alice")  # Output: Hello, Alice

# To provide values inside a funciton, we use parameters (placeholders)


def profile2(n1, a1):
    name = n1
    age = a1
    print("My name is", name, "and my age is", age)


profile2("Ben", 25)  # Output: My name is Ben and my age is 25
profile2("Catherine", 29)  # Output: My name is Catherine and my age is 29
profile2("David", 35)  # Output: My name is David and my age is 35

# ======================================================

# Function with return value


def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)
print("Sum is:", result)  # Output: Sum is: 8

# ======================================================

# Functions with local variables


def adding(a, b):
    ans = a + b  # ans is a local variable
    print(ans + 5)  # Output: 12 if a=3, b=4
    c = 67  # ans is returned to the caller (place where function was called)
    return ans


print(adding(3, 4))    # Output: 7
# print(ans + 5) # TypeError: can only concatenate list (not "int") to list
# print(c)  # Raises NameError since c is local to adding()

# ======================================================

# Types of function arguments:

# 1. Positional arguments:


def profile3(name, age, place):  # Positional parameters
    print(f"My name is {name}. I am {age} years old and I live in {place}.")
    # f strings allow embedding expressions inside string literals


name1 = "Anton"
age1 = 31
place1 = "England"

profile3(name1, age1, place1)  # Calling with positional arguments

# Output: My name is Anton. I am 31 years old and I live in England.

# If the order of parameters is the same as the order of arguments, positional arguments work fine.
# However, if the order is different, it can lead to incorrect results.
# profile3(place1, name1, age1)  # Incorrect order of arguments

# 2. Keyword arguments:

# To overcome the disadvantage of positional arguments, we can use keyword arguments.

profile3(age=age1, place=place1, name=name1)  # Calling with keyword arguments
# Output: My name is Anton. I am 31 years old and I live in England.
# Here, the order of arguments does not matter since we are using keywords.


# 3. Default arguments:

def profile4(name, age, place="Unknown"):  # Default parameter for place
    print(
        f"My name is {name}. I am {age} years old and I live in {place}.")


profile4("Anton", age1)
# Output: My name is Anton. I am 31 years old and I live in Unknown.
# If no default is set, this will raise TypeError since place argument is missing


# 4. Variable-length arguments:
# 5. Keyword-variable length arguments:
