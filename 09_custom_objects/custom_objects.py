"""
Custom Objects in Python: 
Special Methods, Operator Overloading, Static and Class Methods, Prototypes, and Mixins
"""

# ! -------------------------------------------------------------------------------------------

# ! SPECIAL METHODS & OPERATOR OVERLOADING

# ! -------------------------------------------------------------------------------------------

l1 = [1, 2, 3]
print(len(l1))  # ? Output: 3
# This looks like a function call, but internally, Python does this:
# ? len() --> __len__()

# Shows the attributes and methods of the len function, which includes
# the __len__ method that is called when we call the len() function on an object:
print(dir(len))

# list() has a __len__ method defined, which is called when we call the len() function
# on a list object. This is an example of polymorphism.
# The built-in len() function works on different object types because each type defines
# its own __len__ method.

# ? This looks like a simple arithmetic operation:
a = 7
print(a + 3)  # ? Output: 10

# ? But internally, Python does this:
print(a.__add__(3))  # ? Output: 10
# So the + operator is overloaded to perform addition by calling the
# __add__ method of the integer object.

# ? -------------------------------------------------------------------------------------------

# ? Example of operator overloading in a user-defined class:


class Shopping:
    def __init__(self, items):
        # Store the items as a list inside the object (to easily manage/count items)
        self.item = list(items)

    def __len__(self):
        # __len__ is a special (dunder) method.
        # Python automatically calls this method when we use len(object).

        # So when we write: len(s)
        # Python internally does: s.__len__()

        # Here we return twice the actual number of items
        # just to demonstrate that we can control what len() returns.
        return len(self.item) * 2


# Create an object of the Shopping class
s = Shopping(["milk", "bread", "eggs"])

# Calling len(s) automatically triggers s.__len__()
print(len(s))  # Output: 6 (because 3 items * 2)

# dir(list) shows all available methods for the list class, including __len__
print(dir(list))

l1 = [1, 2, 3]

# If the Shopping class did not define __len__, calling len(s) would raise:
# TypeError: object of type 'Shopping' has no len()

# By defining __len__, we allow our custom class to work with Python's built-in len() function.


# ! -------------------------------------------------------------------------------------------

# ! METHOD REDEFINITION AND SIMULATING METHOD OVERLOADING

# ! -------------------------------------------------------------------------------------------

# ? Method redefinition (overwriting inside the same class):

class Summing:
    def adding(self, a, b, c):
        print(a + b + c)

    def adding(self, a, b):
        print(a + b)


s = Summing()

# s.adding(1, 2, 3)
# Gives error because the second adding method overwrites the first adding method,
# so we cannot call the first adding method with three parameters.

# This would work
s.adding(1, 2)  # ? Output: 3

# We can still make it possible:


class Summing2:
    def adding(self, a=0, b=0, c=0):
        # Fails if any of a, b, or c is 0 (or any falsy value)
        if a and b and c:
            print(a + b + c)
        elif a and b:
            print(a + b)
        else:
            print(a)


s = Summing2()

s.adding(1, 2, 3)  # ? Output: 6
s.adding(1, 2)  # ? Output: 3
s.adding(1)  # ? Output: 1


# ! ------------------------------------------------------------------------------------------------

# ! STATIC METHODS & CLASS METHODS

# ! ------------------------------------------------------------------------------------------------

# ? Instance methods:
# Instance methods are the most common type of methods in Python classes.
# They take self as the first parameter, which refers to the instance of the class.
# They can access and modify the instance attributes and can also call other instance methods.


class Individual:
    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print(f"This is an instance method. My name is {self.name}.")


# Create an instance of the Individual class with the name "Tom"
s1 = Individual("Tom")

# Call the instance method using the instance s1
s1.instance_method()
# ? Output: This is an instance method. My name is Tom.

# Error because the instance method cannot be called on the class itself without an instance:
# Individual.instance_method()

# ? ------------------------------------------------------------------------------------------------

# ! Class methods:
# ? Class methods are methods that take cls as the first parameter, which refers to the class
# ? itself. They are defined using the @classmethod decorator. Class methods can access and modify
# ? class attributes, but they cannot access instance attributes directly.


class Individual2:
    school = "ABC School"  # Class attribute (shared across all instances)

    @classmethod
    def student_profile(cls):
        # cls is a convention for the first parameter of a class method, similar to how self is a
        # convention for the first parameter of an instance method. It refers to the class itself
        # and allows us to access class attributes and other class methods.
        print(cls.school)

    def individual3(self):
        # Creates an instance attribute with the same name as the class attribute
        # This does not change the class attribute
        self.school = "XYZ School"
        print(self.school)
        # ? Output: XYZ School
        # (instance attribute takes priority over class attribute within this method)

    def school2(self):
        # Attribute lookup checks the instance first,
        # then falls back to the class if not found
        print(self.school)

    # Runs once when the class is defined
    print("Direct print:", school)


# Create instance
s1 = Individual2()  # ? Output: Direct print: ABC School

# Call class method (via instance)
# This is allowed, but they still receive the class (cls), not the instance.
s1.student_profile()  # ? Output:ABC School

# Modify class attribute (affects all instances unless shadowed)
Individual2.school = "WER School"

s1.student_profile()  # ? WER School


# Create instance attribute (shadows class attribute for this object)
s1.individual3()  # ? Output: XYZ School

s1.school2()  # ? Output: XYZ School (instance attribute takes priority)


# Incorrect call: class method does not accept extra arguments
# Individual2.student_profile("TOM")  # ? TypeError


# Create another instance
student = Individual2()

# Create a new instance attribute for this object only
student.school = "PQR School"

print(student.school)        # ? Output: PQR School (instance attribute)
print(Individual2.school)    # ? Output: WER School (class attribute)


# Incorrect call via instance with extra argument
# s1.student_profile("Harry")  # ? TypeError


# Class attribute remains unchanged
print(Individual2.school)  # ? Output: WER School

# ? ------------------------------------------------------------------------------------------------

# ! Static methods:
# ? Static methods are methods that do not take self or cls as the first parameter.
# ? They are defined using the @staticmethod decorator.
# ? Static methods cannot access or modify instance attributes or class attributes.
# ? Used for utility functions that perform a task in isolation from the class and its instances.

# Static methods belong to a class logically but do not use or modify class or instance state.


class Calc:

    @staticmethod  # Decorator, which does not take self or cls as the first parameter
    def add(a, b):
        return (a + b)


c1 = Calc()


# Call static method using an instance (not recommended but works)
print(c1.add(2, 3))  # ? Output: 5

# Call static method using the class name (standard way to call static methods):
print(Calc.add(5, 3))  # ? Output: 8

# This is an example of a static method because the add method does not take self or cls as the
# first parameter and does not access or modify any instance attributes or class attributes.
# It is a utility function that performs a task (adding two numbers) in isolation from the class
# and its instances.
print(Calc.add(10, 20))  # ? Output: 30


# ! ------------------------------------------------------------------------------------------------

# ! PROTOYPES

# ! ------------------------------------------------------------------------------------------------

# ? Prototypes can create new objects based on existing objects (in JavaScript, not Python).
# ? In Python, we typically use classes and inheritance to achieve similar functionality.

# ? They allow us to create new objects that inherit the properties and methods of the existing
# ? objects without having to define a new class.

# ? Example 1:


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print(self.brand, "car has a speed of", self.speed)


c1 = Car("Toyota", 150)
c2 = Car("Honda", 200)

c1.start()
c2.start()

# ? Output:
# ? Toyota car has a speed of 150
# ? Honda car has a speed of 200

# Car class is the prototype for both c1 and c2 objects.
# Both objects have the same structure and behaviour, only the data changes.

# ! ------------------------------------------------------------------------------------------------

# ! MIXINS

# ! ------------------------------------------------------------------------------------------------

# ? Mixins are a way to add extra functionality to a class using multiple inheritance.
# They are a type of multiple inheritance where a class can inherit from multiple classes, but only
# one of them is the main class, and the others are mixins that provide additional functionality.
# Mixins add specific functionality to a class without affecting main class's structure/behavior.

# ? Advantages of mixin classes:
# - Code Reusability: Mixins allow us to reuse code across multiple classes without having to
#   define the same methods in each class.
# - Separation of Concerns: Mixins help to separate different functionalities into different
#   classes, making the code more organized and easier to maintain.
# - Flexibility: Mixins provide a flexible way to add functionality to classes without being
#   constrained by a strict inheritance hierarchy, allowing for more modular & adaptable code.

# ? ------------------------------------------------------------------------------------------------

# ? Example 1: Creating a mixin class for logging functionality and using it in a Student class.


class Logging:
    """Mixin class that provides logging functionality"""

    def message(self, msg):
        print("Message -", msg)


class Student(Logging):  #
    """Class that inherits from the Logging mixin to gain logging functionality"""

    def __init__(self, name):
        self.name = name


s1 = Student("Tim")
s1.message("Student created")
# ? Output: Message - Student created

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Creating a mixin class for authentication and using it in a class.


class Authentication:
    """Mixin class that provides authentication functionality"""

    def auth(self, user):
        if user == "admin@123":
            return True
        else:
            return False


class OriginalData(Authentication):
    """Class that inherits from the Authentication mixin to gain authentication functionality"""

    def data(self, user_name):
        # This will call the auth method from the Authentication mixin
        if self.auth(user_name):
            print("Access granted to original data")
        else:
            print("Access denied to original data")


d = OriginalData()
d.data("admin@123")
# ? Output: Access granted to original data

d.data("user@123")
# ? Output: Access denied to original data
