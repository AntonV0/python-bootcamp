"""Functions, Modules, and Packages in Python"""

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

# ======================================================

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

# ======================================================

# 2. Keyword arguments:

# To overcome the disadvantage of positional arguments, we can use keyword arguments.

profile3(age=age1, place=place1, name=name1)  # Calling with keyword arguments
# Output: My name is Anton. I am 31 years old and I live in England.
# Here, the order of arguments does not matter since we are using keywords.

# ======================================================

# 3. Default arguments:


def profile4(name, age, place="Unknown"):  # Default parameter for place
    print(
        f"My name is {name}. I am {age} years old and I live in {place}.")


profile4("Anton", age1)
# Output: My name is Anton. I am 31 years old and I live in Unknown.
# If no default is set, this will raise TypeError since place argument is missing

# profile4(name=name1, age=age1, "UK") # Overriding default value
# SyntaxError: positional argument follows keyword argument

profile4(name=name1, age=age1, place="UK")
# My name is Anton. I am 31 years old and I live in UK.

# ======================================================

# 4. Variable-length arguments:

# These allow passing a multiple number of arguments to a single parameter.

# Method 1:


def profile5(*names):  # Asterisk (*) indicates variable-length arguments
    print("My name is:", names)

    for i in names:
        print("Profile 5: My name is: ", i)


names = ["Anton", "Ben", "Catherine", "Diana"]
print(names)  # ['Anton', 'Ben', 'Catherine', 'Diana']

profile5(["Anton", "Ben", "Catherine"])
# Output: Profile 5: My name is:  ['Anton', 'Ben', 'Catherine']
# Note the comma, indicating it's a tuple with one element

# Method 2:


def profile6(age, *names):  # positional argument must come first

    for i in names:
        print("Profile 6: My name is ", i, age)


profile6(30, "Anton", "Ben", "Catherine")
# Output:
# Profile 6: My name is  Anton 30
# Profile 6: My name is  Ben 30
# Profile 6: My name is  Catherine 30

# Method 3


def profile7(age=28, *names):  # You can pass a default value also

    for i in names:
        print("Profile 7: My name is ", i, age)


profile7("Anton", "Ben", "Catherine")  # age is assigned "Anton"

# Output:
# Profile 7: My name is  Ben Anton
# Profile 7: My name is  Catherine Anton

# ======================================================

# 5. Keyword-variable length arguments:

# This allows to pass the argument in the form of key-value pairs.


# Method 1:


def about(**profile8):  # Double asterisk (**) indicates keyword-variable length arguments
    print(profile8)  # {'name': 'Anton', 'age': 31, 'place': 'England'}


about(name="Anton", age=31, place="England")

# Method 2:


def about2(place, phone="07123456789", **profile9):  # Positional argument must come first
    print(profile9, place, phone)


about2("France", name="John", age=50)
# Output: {'name': 'John', 'age': 50} France 07123456789

# ======================================================

# Scope of variables:

# ======================================================

# Global scope:

# When a variable is defined outside any function, it has a global scope.

x = 10  # Global variable

# The global variable can be accessed everywhere in the module, below the line where it is defined.
# Global variables can also be accessed inside functions, but to modify them inside functions,
# we need to use the 'global' keyword.

# ======================================================

# Local scope:

# When a variable is defined inside a function, it has a local scope.
# It can only be accessed within that function.


def local_scope():
    y = 5  # Local variable
    print(y)
    # x = 20 # Local variable, value reassigned to global variable 'x'
    # print(x)  # Error if 'x' is reassigned locally without 'global' keyword
    global x  # Declare 'x' as global to modify it
    x = x + 20  # Output: 30 if global x was 10
    print(x)
    global z
    z = 75  # 'z' is now a global variable


local_scope()  # Output: 5
# print(y)  # Raises NameError since y is local to local_scope()
print(z)  # Output: 75, z is global now
z = 5
print(z)  # Output: 5, z is reassigned globally

# ======================================================

# Enclosed scope:

# A nested function can access variables from its enclosing function.


def outer_function():
    g = 99  # Enclosing variable
    h = 22  # Local variable to outer_function

    def inner_function():
        print(g)  # Accessing enclosing variable
        nonlocal h  # Declare 'h' as nonlocal to modify it, not global
        # 'h' is not defined globally, but in the enclosing function
        h = h + 10
        print(h)
    inner_function()  # Calling inner function from outer function


outer_function()  # Output: 99 (for g), 32 (for h)


# ======================================================

# Built-in scope:

# Built-in scope contains names such as keywords, functions, exceptions that are built into Python.
# These names can be accessed from any part of the code.

print(len("Hello"))  # Output: 5, len() is a built-in function

# If a variable is defined with the same name as a built-in name,
# it will override the built-in name in the current scope.

len = 10  # Overriding built-in name 'len'
print(len)  # Output: 10
# print(len("Hello"))  # Raises TypeError since len is now an integer
