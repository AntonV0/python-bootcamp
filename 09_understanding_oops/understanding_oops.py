"""OOPS - Object-Oriented Programming System"""

import copy
from abc import ABC, abstractmethod
from unicodedata import name

# ! ------------------------------------------------------------------------------------------------

# ! OOPS is a programming paradigm that uses "objects" to design applications and computer programs.

# ! ------------------------------------------------------------------------------------------------

# ? OOPS = Object-Oriented Programming System
# ? It utilises several techniques from previously established paradigms, including modularity,
# ? polymorphism, and encapsulation.

# ? The main goal of OOPS is to bind together the data and the functions that operate on them so
# ? that no other part of the code can access this data except that function.

# ? ------------------------------------------------------------------------------------------------

# ? Example: Calculator app without using classes


def arithmetic():
    """Calculator app without using classes."""

    def add():
        print(2 + 8)
    add()

    def sub():
        # This will not perform subtraction because it is a string, not an expression
        print("10 - 5")
    sub()

    def mul():
        print(5 * 6)
    mul()

    def div():
        print(2 / 3)
    div()


arithmetic()

# ? Output:
# ? 10
# ? 10 - 5 (string, not performing subtraction)
# ? 30
# ? 0.6666666666666666

# This is not a good way to create a calculator app because we have to define the functions for each
# operation and call them separately.
# This is not efficient and also not reusable. We can use classes to create a better calculator app.

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Calculator app using classes


class Calculator:  # Define a class named Calculator
    """Calculator app using classes."""

    def add(self, a, b):
        """Add method"""
        # self is a reference to the current instance of the class,
        # and it is used to access the attributes and methods of the class.
        return a + b

    def sub(self, a, b):
        """Subtract method"""
        return a - b

    def mul(self, a, b):
        """Multiply method"""
        return a * b

    def div(self, a, b):
        """Divide method"""
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed"


calc = Calculator()  # Create an object of the Calculator class
print(calc.add(2, 8))  # Call the add method of the Calculator class
print(calc.sub(10, 5))  # Call the sub method of the Calculator class
print(calc.mul(5, 6))  # Call the mul method of the Calculator class
print(calc.div(2, 3))  # Call the div method of the Calculator class

# ? Output:
# ? 10
# ? 5
# ? 30
# ? 0.6666666666666666

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Human class with attributes and methods


class Human:
    """Human class with attributes and methods."""
    legs = 2
    hands = 2
    eyes = 2
    ears = 2
    nose = 1
    brain = 1

    # self should always be the first parameter of the method in a class
    def dancing(self, about, name):
        """Dancing method of the Human class."""
        print(name, "can dance", about)
        # Print the name and the type of dancing (about) that the human can do

    def speak(self, about, name):
        """Speak method of the Human class."""
        print(name, "can speak", about)
        # Print the name and the language (about) that the human can speak

    def laugh(self, about, name):
        """Laugh method of the Human class."""
        print(name, "can laugh", about)
        # Print the name and the type of laugh (about) that the human can do


anton = Human()  # Create an object of the Human class
print(anton.legs)  # Access the legs attribute of the Human class
# ? Output: 2

john = Human()  # Create another object of the Human class
bob = Human()

anton.dancing("fast", "Anton")  # Call the dancing method of the Human class
# ? Output: Anton can dance fast

john.speak("English", "John")  # Call the speak method of the Human class
# ? Output: John can speak English

bob.laugh("loudly", "Bob")  # Call the laugh method of the Human class
# ? Output: Bob can laugh loudly

# ! ------------------------------------------------------------------------------------------------

# ! CLASSES:

# ! ------------------------------------------------------------------------------------------------

# ? A class in python is a blueprint for creating objects. It defines a set of attributes and
# ? methods that the objects created from the class will have.

# We can create a class and then create objects of that class to use its attributes and methods.

# The Class concept is mainly used for reusability of code.
# We can create an object of a class and use it whenever we want.
# We can also create multiple objects of a class and use them in different parts of the code.
# Every class has its own namespace. Its attributes and methods are accessed through the class
# name or its instances (objects).

# ? ------------------------------------------------------------------------------------------------

# ? Example 1: Creating a class with attributes and accessing them through an object


class Student:
    """Student class with attributes."""
    name1 = "Harry"
    age1 = 23
    # Accessing class attributes directly within the class definition
    print(name1, age1)  # This runs once when the class is defined
    # ? Output: Harry 23

# print(name1, age1)
# This will give an error because name1 and age1 are not defined in the global namespace


# Accessing class attributes using the class name outside the class definition
print(Student.name1, Student.age1)
# ? Output: Harry 23

harry_object = Student()  # Create an object of the Student class
# The process of creating an object from a class is called instantiation.
# The object is an instance of the class.
print(harry_object.name1, harry_object.age1)
# ? Output: Harry 23

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Creating a method inside a class


class StudentProfile:
    """StudentProfile class with a method."""

    # Python automatically passes the instance as the first argument (self)
    def profile(self):  # Could also do `profile(StudentProfile)` but `self` is more commonly used
        """profile method of the StudentProfile class."""
        name1 = "Jack"
        percentage = 86
        print(name1, percentage)


# Create an object (instance) of the StudentProfile class
jack_object = StudentProfile()
# Call the profile method of the StudentProfile class using the object
jack_object.profile()
# ? Output: Jack 86

# ? ------------------------------------------------------------------------------------------------

# ? Note: The `self` parameter acts as a mapping to the instance of the class (object)
# ? that is calling the method.

# When we call the profile method using the jack_object, the self parameter will refer
# to the jack_object instance of the StudentProfile class.
# If we define the profile method without the self parameter, it will not work when we call it
# using the object because it will not have a reference to the instance of the class that is
# calling the method.

# ? Using self:
# - Keeps data tied to each object
# - Allows multiple instances to exist independently
# - Enables polymorphism and inheritance
# - Makes your class reusable and scalable

# Using the class name accesses class-level attributes.
# Using self allows instance-level flexibility and supports inheritance.

# ? Using class name instead of self:
# - Creates shared state (all instances share the same data)
# - Can break encapsulation (all instances can access and modify the same data)
# - Can cause subtle bugs (difficult to track which instance is modifying the data)

# ? ------------------------------------------------------------------------------------------------

# ? RAM (Random Access Memory) is used to store the data and instructions that the CPU
# ? (Central Processing Unit) needs to access quickly.

# When we create an object of a class, it is stored in the RAM and it has a unique memory address.

print(id(harry_object))  # ? 1553595157536
print(id(jack_object))  # ? 1553595157872 - different ID for different object

# ? Stacks are used to store the function calls and local variables. Python abstracts this.
# When we call a method of a class, it is stored in the stack and it has a unique memory address.

# ? Heaps are used to store the objects created from a class.
# When we create an object of a class, it is stored in the heap and it has a unique memory address.

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Parameterised method in a class


class Calculator2:
    """Calculator class with a parameterised method."""

    def add(self, a, b):
        """Add method of the calculator class that takes two parameters."""
        return a + b

    def subtract(self, a, b):
        """Subtract method of the calculator class that takes two parameters."""
        return a - b


calculation_object = Calculator2()  # Create an object of the calculator class
# Call the add method of the calculator class using the object and passing arguments
print(calculation_object.add(10, 5))
# ? Output: 15
# Call the subtract method of the calculator class using the object and passing arguments
print(calculation_object.subtract(10, 5))
# ? Output: 5

# ? ------------------------------------------------------------------------------------------------

# ? Example 4: Class with attributes and a method that accesses those attributes


class Cart:
    """Cart class with attributes and a method."""
    name = "Mobile"
    price = 7500
    company = "apple"

    def display(self):
        """Display method of the Cart class."""
        print(self.name, self.price, self.company)
        # Alternatively, we could also use Cart.name, Cart.price, Cart.company
        # But using self is more common and it allows us to access the attributes
        # of the class through the object that is calling the method.


cart_object = Cart()
cart_object.display()
# ? Output: Mobile 7500 apple

# ? ------------------------------------------------------------------------------------------------

# ? Example 5: Method that takes parameters to display the attributes of the class


class Laptop:
    """Laptop class with a method that takes parameters to display the attributes of the laptop."""

    def configs(self, colour, company, price):
        """Configs method of the Laptop class."""
        # print(self.colour, self.company, self.price)
        # - would give error because these attributes are not defined in the class
        print(colour, company, price)


dell = Laptop()
dell.configs("black", "Dell", 50000)
# ? Output: black Dell 50000

# ? ------------------------------------------------------------------------------------------------

# ? Example 6: Instance variables (attributes) assigned to the class through a method


class Employee:
    """Employee class with a method that assigns attributes to the class."""

    def profile(self):  # Instead of this, best practice is to use def __init__(self)
        """Profile method of the Employee class."""
        # Instance variable (attribute) assigned to this instance of the class
        self.name = "Alice"
        self.age = 30  # Another instance variable


e1 = Employee()  # Create an object of the Employee class
e1.profile()  # Call the profile method to assign attributes to the class
print(e1.name, e1.age)
# ? Output: Alice 30

# ! ------------------------------------------------------------------------------------------------

# ! CONSTRUCTORS (__init__)

# ! ------------------------------------------------------------------------------------------------

# ? A constructor is a special method in a class that is automatically called when an object of the
# ? class is created. It is used to initialise the attributes of the instance.

# The constructor method in Python is called __init__() and it takes self as the first parameter,
# followed by any other parameters that we want to use to initialise the attributes of the instance.

# ? ------------------------------------------------------------------------------------------------

# ? Example 1: Creating a class with a constructor that prints a message when an object is created


class CSE:
    """CSE class with a constructor that prints a message when an object of the class is created."""

    def __init__(self):  # __init__ is the constructor method of the CSE class
        print("CSE class constructor called")


c1 = CSE()  # Create an object of the CSE class
# ? Output: CSE class constructor called
# This is the correct initialisation
# (constructor method automatically called when object is created)

c1.__init__()  # Call the constructor method of the CSE class using the object
# ? Output: CSE class constructor called
# This is not wrong, but it is not normal practice.
# It is meant to be automatically called when the object is created.
# It should not be called explicitly.

# ? ------------------------------------------------------------------------------------------------

# ? Example 2:  Creating a class with a parameterised constructor


class Vegetables:
    """Vegetables class with a parameterised constructor."""

    # Parameterised constructor that takes three parameters
    def __init__(self, colour, taste, price):
        print(colour, taste, price)
        # This does not assign attributes, so the object does not store these values


Tomato = Vegetables("Red", "Sweet", 30)  # Passing arguments to the constructor
# ? Output: Red Sweet 30

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Method overwrtiting by defining multiple __init__ methods in the same class


class Cars:
    """Cars class with multiple __init__ methods (not allowed in Python)."""

    def __init__(self, colour):
        print(colour, "car")  # This cannot be accessed

    def __init__(self):  # No parameters passed to the constructor
        print("Colour not found")

# BMW = Cars("Black")
# Results in an error due to method overwriting, as the second __init__ method overwrites the first.

# ? ------------------------------------------------------------------------------------------------

# ? Example 4 - Using a method to assign attributes to the instance instead of a constructor


class Bikes:
    """Bikes class with a method to assign attributes to the instance."""

    def details(self):
        self.name = "Dugati"
        self.owner = "John"

    def engine(self, cc, torque, fuel):
        print(self.name, self.owner, cc, torque, fuel)

    def identity(self, colour, make, model):
        print(self.name, self.owner, colour, make, model)


Dugati = Bikes()  # Create an object of the Bikes class
# Call the engine method of the Bikes class using the object

Dugati.details()  # Call the details method to assign attributes to the instance

# Passing parameters to the engine method of the Bikes class using the object
Dugati.engine(650, 80, "Petrol")
# ? Output: Dugati John 650 80 Petrol

# Passing parameters to the identity method of the Bikes class using the object
Dugati.identity("Green", "Dugati", "2024")
# ? Output: Dugati John Green Dugati 2024

# ? ------------------------------------------------------------------------------------------------

# ? Example 5 - Using a constructor to assign attributes to the class instead of a separate method


class Bikes2:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        # return self.name, self.owner
        # This will give an error because __init__ must return None.
        # Returning any value other than None raises a TypeError.

    def engine(self, cc, torque, fuel):
        print(self.name, self.owner, cc, torque, fuel)

    def identity(self, colour, make, model):
        print(self.name, self.owner, colour, make, model)


name = input("Enter the name of the bike: ")
owner = input("Enter the name of the owner: ")

# Pass parameters to the constructor to assign attributes to the class
Dugati = Bikes2(name, owner)

Dugati.engine(650, 80, "Petrol")
Dugati.identity("Green", "Dugati", "2024")

# ? Example output:
# Enter the name of the bike: Dugati
# Enter the name of the owner: John
# Dugati John 650 80 Petrol
# Dugati John Green Dugati 2024

# ! ------------------------------------------------------------------------------------------------

# ! ALIASING, SHALLOW & DEEP COPY

# ! ------------------------------------------------------------------------------------------------

# ! Aliasing:

# ? Aliasing means two variables point to the same object in memory.
# ? Any change through one name affects the other, because it's the same list.

list1 = [1, 2, 3, [4, 5], [6, 7, 8]]
list2 = list1  # alias (not a copy)

list2.append("hello")

print(list1)          # ? [1, 2, 3, [4, 5], [6, 7, 8], 'hello']
print(list2)          # ? [1, 2, 3, [4, 5], [6, 7, 8], 'hello']
print(id(list1))      # ? 2774036278656
print(id(list2))      # ? 2774036278656

# ? ------------------------------------------------------------------------------------------------

# ! Shallow Copy:

# ? A shallow copy creates a new outer object,
# ? but nested objects inside are still shared references.

# import copy (top of the file)

list3 = [1, 2, 3, [4, 5], [6, 7, 8]]
list4 = list3.copy()  # Creates a shallow copy (new outer list)

print(id(list3))      # ? different id
print(id(list4))      # ? different id

# Changing the outer list affects only the copy:
list4.append("hello there")
print(list3)          # ? [1, 2, 3, [4, 5], [6, 7, 8]]
print(list4)          # ? [1, 2, 3, [4, 5], [6, 7, 8], 'hello there']

# But changing a nested list affects both (nested lists are shared):
list4[3].append("Ice Cream")
print(list3)          # ? [1, 2, 3, [4, 5, 'Ice Cream'], [6, 7, 8]]
# ? [1, 2, 3, [4, 5, 'Ice Cream'], [6, 7, 8], 'hello there']
print(list4)

# ? ------------------------------------------------------------------------------------------------

# ! Deep Copy:

# ? Deep copy creates a new outer object and new nested objects.
# ? Nothing is shared, so changes do not affect the original.

# import copy (top of the file)

list5 = [1, 2, 3, [4, 5], [6, 7, 8]]
list6 = copy.deepcopy(list5)
# This creates a deep copy of list5, so list6 and the nested lists are also new objects

list6[3].append("Ice Cream")
print(list5)  # ? Output: [1, 2, 3, [4, 5], [6, 7, 8]]
print(list6)  # ? Output: [1, 2, 3, [4, 5, 'Ice Cream'], [6, 7, 8]]
# Modifying the nested list in list6 does not modify the nested list in list5 because they are
# referencing different nested lists in memory

# ? ------------------------------------------------------------------------------------------------

# ? Example - Shallow vs Deep Copy with a class:

# import copy (top of the file)


class Student2:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)


# Original object
s1 = Student2("Alice", [85, 90, 95])

# ? Shallow copy
# Modifying the marks in s2 will modify the marks in s1 since they reference the same list in memory
s2 = copy.copy(s1)
s2.marks[0] = 100  # This affects s1 because s2 is a shallow copy of s1

print("After shallow copy change:")
s1.display()  # ? Output: Alice [100, 90, 95]
s2.display()  # ? Output: Alice [100, 90, 95]

# ? Deep copy
# This creates a deep copy of s1, so s3 is a new object and the marks list is also a new object
s3 = copy.deepcopy(s1)
s3.marks[0] = 50  # This does not affect s1 because s3 is a deep copy of s1

print("\nAfter deep copy change:")
s1.display()  # ? Output: Alice [100, 90, 95]
s3.display()  # ? Output: Alice [50, 90, 95]

# We can show the difference between shallow copy and deep copy by modifying the marks in s2 and s3
# and then displaying the marks in s1, s2, and s3 to see the difference:
s2.marks[0] = 80
s3.marks[0] = 70

s1.display()  # ? Output: Alice [80, 90, 95]
s2.display()  # ? Output: Alice [80, 90, 95]
s3.display()  # ? Output: Alice [70, 90, 95]

# This shows that modifying the marks in s2 also modified the marks in s1 because they are
# referencing the same list in memory (shallow copy), while modifying the marks in s3 did not
# modify the marks in s1 because they are referencing different lists in memory (deep copy).

# ! ------------------------------------------------------------------------------------------------

# ! INHERITANCE

# ! ------------------------------------------------------------------------------------------------

# ? Inheritance is the process by which one class (called the child class or subclass) can
# ? inherit the attributes and methods of another class (called the parent class or superclass).

# ? Types of inheritance in Python:
# - single inheritance
# - multilevel inheritance
# - multiple inheritance
# - hierarchical inheritance
# - hybrid inheritance

# ! ------------------------------------------------------------------------------------------------

# ! Single inheritance

# ? In single inheritance, a single child class inherits from a single parent class.

# ? Example 1: Child Class Inheriting Methods from Parent Class


class TATA:
    def model(self):
        name = "safari"
        colour = "yellow"
        print(name, colour)


class Jaguar(TATA):
    def model2(self):
        name = "jaguar"
        colour = "red"
        print(name, colour)


j1 = Jaguar()  # Create an object of the Jaguar class

j1.model()  # Call the model method of the TATA class using the object of the Jaguar class
# (inherited from the TATA class)
# ? Output: safari yellow

j1.model2()  # Call the model2 method of the Jaguar class using the object of the Jaguar class
# ? Output: jaguar red

# In this example, the Jaguar class is the child class that inherits from the TATA class,
# which is the parent class. The Jaguar class can access the model method of the TATA class
# because it is inherited from the TATA class. The Jaguar class also has its own method called
# model2, which is not inherited from the TATA class.

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Accessing Parent Class Attributes (Class Variables)


class Parent:
    a = 6
    b = 4


class Child(Parent):
    print(Parent.a, Parent.b)  # 6 4 - works

    # print(a, b)
    # # NameError because a and b are not defined in the Child class

    # print(self.a, self.b)
    # Error because self does not exist in the class body, it is only defined in the class methods

    print(Parent.a, Parent.b)
    # This works because we are accessing the attributes of the parent class using class name

    def display(self):
        print(self.a, self.b)
        # This works as we access the attributes of the parent class using the self parameter


c1 = Child()  # Create an object of the Child class

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Inheriting Instance Attributes via Parent Methods


class Parent2:
    def data1(self, x, y):
        self.x1 = x
        self.y1 = y


class Child2(Parent2):
    def data2(self):
        # print(x1, y1)
        # print(parent.x1, parent.y1)
        # Both of these will give an error because x1 and y1 are not defined in the class.
        # They are defined in the data1 method of the Parent2 class, and we cannot access them
        # directly in the Child2 class without creating an object of the Parent2 class and
        # calling the data1 method to assign values to x1 and y1.

        # print(self.x1, self.y1)
        # print (Parent2.x1, Parent2.y1)
        # Both still give an error because we have not called the data1 method to assign values
        # to x1 and y1, so they are not defined in the Child2 class yet.

        # ? Correct way:

        # This will work because we are calling the data1 method of the Parent2 class using the
        # self parameter and passing the arguments to it:
        # print(Parent2.data1(self, 10, 20))
        # Output: None
        # because the data1 method does not return anything, it just assigns the attribute values

        # This is the best way of doing it:
        self.data1(10, 20)
        print(self.x1, self.y1)
        # ? Output: 10 20


c2 = Child2()  # Create an object of the Child2 class
c2.data2()  # Call the data2 method of the Child2 class

# ? ------------------------------------------------------------------------------------------------

# ? Example 4: Parent Constructor Inheritance (__init__ Inheritance) in a Child Class


class C1:
    def __init__(self):
        self.name = "Kim"
        self.age = 40
        print(self.name, self.age)  # ? Output: Kim 40


class C2(C1):
    # print(C1.name, C1.age)

    def display(self):
        print(self.name, self.age)  # ? Output: Kim 40


c = C2()
c.display()

# ! ------------------------------------------------------------------------------------------------

# ! Multilevel inheritance
# ? In multilevel inheritance, a child class inherits from a parent class,
# ? and then another child class inherits from the first child class.

# Class A is the parent class
# Class B is the child class that inherits from Class A
# Class C is the child class that inherits from Class B


class Animal:  # Parent class
    tail = 1
    ears = 2

    def speak(self):
        # This attribute only exists after calling speak() method
        self.voice = "The voice is: "
        print("Animal speaks")


class Dog(Animal):  # Child class that inherits from the Animal class
    def dog_voice(self):
        self.speak()  # Call the speak method of the Animal class using the self parameter
        print(self.voice)  # ? Output: The voice is:
        print("Dog barks")  # ? Output: Dog barks


class Cat(Dog):  # Child class that inherits from the Dog class (a child class of the Animal class)
    def cat_voice(self):
        self.speak()  # Call the speak method of the Animal class using the self parameter
        print("Cat meows")


a1 = Cat()
a1.dog_voice()  # ? Output: Dog barks
a1.cat_voice()  # ? Output: Cat meows
a1.speak()  # ? Output: Animal speaks

b1 = Dog()
b1.dog_voice()  # ? Output: Dog barks
b1.speak()  # ? Output: Animal speaks

# ! ------------------------------------------------------------------------------------------------

# ! Multiple inheritance:
# ? In multiple inheritance, a child class inherits from more than one parent class.
# ? This is Python's unique feature that allows a child class to inherit from multiple
# ? parent classes, which is not allowed in some other programming languages.


class Calc:
    def sum(self, a, b):
        print(a + b)


class Calc2:
    def mul(self, a, b):
        print(a * b)


class Calc3:
    def sub(self, a, b):
        print(a - b)


class Calc4(Calc, Calc2, Calc3):
    def div(self, a, b):
        print(a / b)


c4 = Calc4()
c4.mul(2, 6)  # ? Output: 12

# c4.mul(a, b)
# NameError because a and b are not defined in the class, and we cannot call the mul method of
# the Calc2 class using the class name without creating an object of the Calc2 class.

# But you can call it on the class if you pass an instance manually:
Calc2.mul(c4, 2, 6)   # ? Output: 12
# Works, but not recommended

c4.sub(9, 5)  # ? Output: 4
print(Calc4.__mro__)
# ? Output: (<class '__main__.Calc4'>, <class '__main__.Calc'>,
# ? <class '__main__.Calc2'>, <class '__main__.Calc3'>, <class 'object'>)

# ? Explaining the output of __mro__:
# __mro__ is a Method Resolution Order that shows the order in which the classes are searched when
# we call a method of the child class. It shows that the Calc4 class is searched first, then the
# Calc class, then the Calc2 class, then the Calc3 class, and finally the object class (which is
# the parent class of all classes in Python).

# ! ------------------------------------------------------------------------------------------------

# ! Hierarchical inheritance:
# ? In hierarchical inheritance, multiple child classes inherit from a single parent class.

# ? Example 1: Multiple Child Classes Inheriting from One Parent Class


class Fruits:
    def __init__(self, name, colour):
        pass  # This is a placeholder for the constructor, we can assign the name and colour
        # to the class attributes if we want to use them in the child classes


class Mango(Fruits):
    def taste(self):
        print("Mango is sweet")


class Apple(Fruits):
    def apple_taste(self):
        print("Apple is also sweet")


# Create an object of the Mango class and pass arguments to the constructor of the Fruits class
# This will not store the name and colour in the Mango class
m1 = Mango("Mango", "Yellow")
# (due to pass in the constructor)
m1.taste()
# ? Output: Mango is sweet

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Sharing Parent Constructor and Attributes Across Multiple Child Classes


class Fruits2:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


class Mango2(Fruits2):
    def taste(self):
        print(self.name, "is", self.colour)  # Mango is Yellow
        print("Mango is sweet")


class Apple2(Fruits2):
    def apple_taste(self):
        print(self.name, "is", self.colour)  # Apple is Red
        print("Apple is also sweet")


# Create an object of the Mango class and pass arguments to the constructor of the Fruits class
m1 = Mango2("Mango", "Yellow")
m1.taste()

a1 = Apple2("Apple", "Red")
a1.apple_taste()

# ? Output:
# ? Mango is Yellow
# ? Mango is sweet
# ? Apple is Red
# ? Apple is also sweet

# ! ------------------------------------------------------------------------------------------------

# ! Hybrid inheritance:
# ? In hybrid inheritance, a child class inherits from multiple parent classes,
# ? and those parent classes may also have their own parent classes.
# ? This is a combination of multiple inheritance and multilevel inheritance.


class D1:
    def m1(self):
        print("This is method 1 of class D1")


class D2(D1):
    def m2(self):
        print("This is method 2 of class D2")


class D3(D2):
    def m3(self):
        print("This is method 3 of class D3")


class D4(D1):
    def m4(self):
        print("This is method 4 of class D4")


class D5(D4, D2):
    def m5(self):
        print("This is method 5 of class D5")


obj5 = D5()  # Create an object of the D5 class
obj5.m5()  # ? Output: This is method 5 of class D5
obj5.m4()  # ? Output: This is method 4 of class D4
obj5.m2()  # ? Output: This is method 2 of class D2
obj5.m1()  # ? Output: This is method 1 of class D1

# In this example, the D5 class inherits from both D4 and D2, which are child classes of D1.
# The D3 class is a child class of D2, which is a child class of D1. This creates a hybrid
# inheritance structure where the D5 class can access methods from both D4 and D2, as well as
# the methods from D1 through both parent classes.

# ! ------------------------------------------------------------------------------------------------

# ! POLYMORPHISM

# ! ------------------------------------------------------------------------------------------------

# ! Polymorphism is the ability of an object to take on many forms.
# ? It allows us to use a single interface to represent different types of objects.

# ? In Python, polymorphism is achieved through method overriding, where a child class can provide
# ? a specific implementation of a method that is already defined in its parent class.

# ? It is a single method or operator that can perform multiple operations based on the context.

# ? Polymorphism in builtin functions:
# len() --> can return the length of objects like strings, lists, tuples, etc.
# update() --> can update the values of objects like dictionaries, sets, etc.
# pop() --> can remove an element from objects like lists, sets, etc.
# max() --> can return the maximum value from objects like lists, tuples, etc.
# min() --> can return the minimum value from objects like lists, tuples, etc.
# type() --> can return object type like integers, floats, strings, lists, etc.

# ? Polymorphism in operators:
# + --> polymorphic operator (can perform addition on objects)
# * --> polymorphic operator (can perform multiplication on objects)
# / --> polymorphic operator (can perform division on objects)
# - --> polymorphic operator (can perform subtraction on objects)

l1 = [1, 2, 3]
l2 = [3, 4]

# In this case, the + operator is used to concatenate two lists:
print(l1 + l2)
# ? Output: [1, 2, 3, 3, 4]

# In this case, the * operator is used to repeat the string s1 two times:
s1 = "Hello"
# ? Output: HelloHello
print(s1 * 2)

# ! ------------------------------------------------------------------------------------------------

# ! Polymorphism in User Defined Classes:

# ? This can be achieved by creating methods in the child class that have the same name as the
# ? methods in the parent class, but with different implementations. This allows us to use the same
# ? method name to perform different operations based on the context of the object.

# ? Polymorphism can be achieved using 2 methods:
# 1. Method overriding (inheritance)
# 2. Method overloading (not supported in Python)
#    - but possible with default arguments or variable length arguments

# ? Polymorphism Using Duck Typing
# Duck typing is a concept in Python where the type or class of an object is less important than the
# methods it defines. If an object has the necessary methods, it can be used in place of another
# object, regardless of their class.

# ? Here are two unrelated classes with the same methods (without overriding or overloading):


class Ferrari:
    def fuel_type(self):
        print("The fuel type of Ferrari is petrol")

    def max_speed(self):
        print("The maximum speed of Ferrari is 350 km/h")


class Lamborghini:
    def fuel_type(self):
        print("The fuel type of Lamborghini is diesel")

    def max_speed(self):
        print("The maximum speed of Lamborghini is 320 km/h")


fer = Ferrari()
lam = Lamborghini()

fer.fuel_type()  # ? Output: The fuel type of Ferrari is petrol
lam.fuel_type()  # ? Output: The fuel type of Lamborghini is diesel
fer.max_speed()  # ? Output: The maximum speed of Ferrari is 350 km/h
lam.max_speed()  # ? Output: The maximum speed of Lamborghini is 320 km/h

# Diffrent objects of different classes, but they have the same methods,
# so we can call the methods using a loop:
for i in fer, lam:
    i.fuel_type()
    i.max_speed()

# ? Output:
# ? The fuel type of Ferrari is petrol
# ? The maximum speed of Ferrari is 350 km/h
# ? The fuel type of Lamborghini is diesel
# ? The maximum speed of Lamborghini is 320 km/h

# ! -------------------------------------------------------------------------------------------

# ! Method Overriding (Polymorphism in Inheritance):


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_role(self):  # This method will be overridden in the child classes
        return f"{self.name} is a person and is {self.age} years old."


class Student3(Person):  # Child class that inherits from the Person class
    def __init__(self, name, age, major, student_id):
        # super() calls the constructor of parent class (Person) to initialise name and age
        super().__init__(name, age)
        self.major = major
        self.student_id = student_id

    def get_role(self):  # This method overrides the get_role method of the Person class
        return f"{self.name} is a student majoring in {self.major} with student ID {self.student_id}."


class Professor(Person):  # Child class that inherits from the Person class
    def __init__(self, name, age, department, employee_id):
        super().__init__(name, age)
        self.department = department
        self.employee_id = employee_id

    def get_role(self):  # This method overrides the get_role method of the Person class
        return f"{self.name} is a professor in the {self.department} department with employee ID {self.employee_id}."


person1 = Person("Alice", 30)
student1 = Student3("Alice", 30, "Computer Science", "12345")
professor1 = Professor("Andrew", 30, "EEE", "54321")

print(person1.get_role())
# ? Output: Alice is a person and is 30 years old.

print(student1.get_role())
# ? Output: Alice is a student majoring in Computer Science with student ID 12345.

print(professor1.get_role())
# ? Output: Andrew is a professor in the EEE department with employee ID 54321.


# ! ------------------------------------------------------------------------------------------------

# ! Abstraction

# ? Abstraction is the process of hiding the implementation details and showing only the
# ? functionality to the user. The user can focus on what the object does instead of how it does it.

# ? Abstract classes act as a blueprint/prototype for other classes.

# ? Abstract classes have control over all the child classes that inherit from it,
# ? and they can force the child classes to implement certain methods.

# ? ------------------------------------------------------------------------------------------------

# ? Example 1: Abstract Class with Abstract Method
# from abc import ABC, abstractmethod (top of the file)

class Shapes(ABC):
    # This is a decorator that is used to declare a method as an abstract method.
    @abstractmethod
    # An abstract method forces child classes to implement this method, and it does not have any
    # implementation in the abstract class.
    # A decorator is a function that takes another function as an argument and extends the behavior
    # of the latter function without explicitly modifying it.
    def number_of_sides(self):
        """Must be implemented by child classes to return the number of sides."""
        pass

# s = Shapes()
# s.number_of_sides()
# Here, we cannot create an object of the Shapes class because it is an abstract class,
# and it is not meant to be instantiated. It is meant to be inherited by other classes that
# will implement the number_of_sides method.


class Triangle(Shapes):
    def number_of_sides(self):
        # The abstract method must be implemented in the child class with a return statement.
        # print("Triangle has 3 sides") # This will return None
        return 3

    def triangle_shape(self):
        print("Triangle is a shape with 3 sides")


class Square(Shapes):
    def number_of_sides(self):
        # The abstract method must be implemented in the child class with a return statement.
        # print("Square has 4 sides") # This will return None
        return 4

    def square_shape(self):
        print("Square is a shape with 4 sides")


triangle = Triangle()
triangle.triangle_shape()  # ? Output: Triangle is a shape with 3 sides
print(triangle.number_of_sides())  # ? Output: 3

square = Square()
square.square_shape()  # ? Output: Square is a shape with 4 sides
print(square.number_of_sides())  # ? Output: 4

# ? ------------------------------------------------------------------------------------------------

# ? SIDENOTE: Method Overriding using super()
# ? (not an abstract class, but shows how to call parent class method in child class)


class Zoo:
    def cage(self):
        print("All animals are in the cage")


class Tiger(Zoo):
    def cage(self):
        super().cage()  # This will call the cage method of the Zoo class using the super()
        # function, which allows us to call a method from the parent class in the child class.
        # This is useful when we want to add some functionality to the method in the child class
        # while still keeping the functionality of the method in the parent class.

        # OR:

        # Create a super object to call methods from the parent class in the child class:
        # s = super()

        # Call the parent class method using the super object:
        # s.cage()
        print("The tiger is out of the cage")


t = Tiger()
t.cage()
# ? Output:
# ? All animals are in the cage
# ? The tiger is out of the cage

# This is method overriding because the cage method is overridden in the Tiger class.
# This allows us to use the same method name (cage) to perform different operations based on the
# context of the object (Tiger or Zoo).

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Abstract Class with Required Method Implementation
# from abc import ABC, abstractmethod (top of the file)


class Circle(ABC):

    @abstractmethod
    def area_of_circle(self, r):
        """No implementation in the abstract class, must be implemented by child classes."""


class Display(Circle):
    """Implementing the abstract method area_of_circle in the Display class."""

    def area_of_circle(self, r):
        area = 3.14 * r ** 2
        print("The area of the circle is:", area)


d1 = Display()
d1.area_of_circle(5)
# ? Output: The area of the circle is: 78.5


# ! ------------------------------------------------------------------------------------------------

# ! Encapsulation:
# ? Encapsulation is the process of hiding the internal details of an object and only exposing
# ? a public interface to the user. This is done to protect the data and methods of the object from
# ? being accessed or modified by outside code.

# ? ------------------------------------------------------------------------------------------------

# ? Example 1: Encapsulation with Public, Protected, and Private Attributes


class Student4:
    name = "Anna"  # Public attribute - can be accessed and modified by outside code
    age = 24  # Public attribute - can be accessed and modified by outside code
    _place = "England"  # Protected attribute - can be accessed and modified by outside code
    __grade = "A"  # Private attribute - cannot be accessed or modified by outside code

    # Within the class, we can access all attributes, including the private attribute __grade:
    print(name, age, _place, __grade)  # ? Output: Anna 24 England A


s4 = Student4()
print(s4.name)  # ? Output: Anna

# This will work, but it is a convention to indicate that it should not be accessed directly:
print(s4._place)  # ? Output: England


# print(s4.__grade)
# AttributeError: 'Student4' object has no attribute '__grade'
# __grade is name mangled to _Student4__grade, and it cannot be accessed directly using __grade

s4.name = "Maria"
print(s4.name)  # ? Output: Maria

# name and age can be accessed and modified by outside code, which is not good for data protection.
# To achieve encapsulation, we can make private attributes like __grade and provide public methods
# to access and modify them, which allows us to control how the data is accessed and modified.

# ? ------------------------------------------------------------------------------------------------

# ? Example 2: Encapsulation with Private Methods:


class Bank:
    def get_ratio(self):
        return "10%"

    def _SBI(self):
        return "8.5%"

    def __HSBC(self):
        return "9.5%"

    def display(self):
        """
        This will work because we are calling the private method __HSBC 
        from within the class using the self parameter
        """
        return self.__HSBC()

    # This will also work because we are calling the private method __HSBC
    # from within the class using the self parameter
    def __init__(self):
        """
        This will also work because we are calling the private method __HSBC 
        from within the class using the self parameter
        """
        print(self.__HSBC())


sbi = Bank()
print(sbi._SBI())  # ? Output: 8.5%

hsbc = Bank()
# This will give an error because __HSBC is a private method and cannot be accessed directly:
# print(hsbc.__HSBC())

# This will work because we are calling the private method __HSBC from within the class
# using the display method:
hsbc.display()  # ? Output: 9.5%

# ? ------------------------------------------------------------------------------------------------

# ? Example 3: Encapsulation with Private Attributes and Public Methods to Access/Modify Them:


class Car:
    __name = ""  # Class-level private attribute

    def __init__(self):
        self.__name = "Kim"  # Initialising the private attribute __name in the constructor
        self.company = "Ford"  # This is a public attribute that can be accessed and modified

    def owner(self):
        # Modifying the private attribute within the class using a public method
        self.__name = "John"

    def display(self):
        # Accessing the private attribute within the class using a public method
        print("The owner of the car is:", self.__name)
        print("The company of the car is:", self.company)

    def change_name(self, owner):
        # This is a public method that allows us to set the value of the private attribute __name
        self.__name = owner
        self.company = "Toyota"


class ChildCar(Car):
    def child_method(self, name1):
        self.change_name(name1)
        self.display()


BMW = Car()
BMW.owner()  # This will set the private attribute __name to "John" using the owner method
BMW.display()  # Prints owner using the display method, which accesses the private attribute __name
# ? Output:
# ? The owner of the car is: John
# ? The company of the car is: Ford

# This will not change the private attribute __name because it is a new attribute created in the
# instance, not the private attribute defined in the class:
BMW.__name = "Alan"

# This will still print the owner of the car as "John" because the private attribute __name
# is not changed by the above line:
BMW.display()
# ? Output:
# ? The owner of the car is: John
# ? The company of the car is: Ford

# This will change the private attribute __name to "Alan" using the change_name method
BMW.change_name("Alan")

# Print the owner of the car using the display method, which accesses the private attribute __name
BMW.display()
# ? Output:
# ? The owner of the car is: Alan
# ? The company of the car is: Toyota

child1 = ChildCar()
# Print the owner of the car using the display method, which accesses the private attribute __name
child1.display()
# ? Output:
# ? The owner of the car is: Kim
# ? The company of the car is: Ford


# This will change the private attribute __name to "David" using the child_method, which calls the
# change_name method of the parent class:
child1.child_method("David")
# ? Output:
# ? The owner of the car is: David
# ? The company of the car is: Toyota

# ? ------------------------------------------------------------------------------------------------

# ? Example 4: Encapsulation, Static Private Attributes, and Name Mangling

# Name mangling is a mechanism in Python that allows us to create private attributes and methods
# in a class by prefixing their names with double underscores (__). This makes them inaccessible
# from outside the class, and they can only be accessed from within the class using name mangling.


class Employee2:
    __place = "India"  # Static private attribute
    # (static because it is shared by all instances of the class, and private because it cannot be
    # accessed directly from outside the class)

    def __init__(self, name, salary):
        self.__name = name  # Instance private attribute
        self.__salary = salary  # Instance private attribute
        self.__place = "UK"  # This will create a new instance attribute __place
        # (shadowing the class attribute __place)

        # This will print the value of the instance attribute __place, which is "UK"
        print(self.__place)
        # ? Output: UK


emp2 = Employee2("Jessica", 50000)

# AttributeError because __name and __salary are private attributes and cannot be accessed directly:
# print(emp2.__name)
# print(emp2.__salary)

# This will work because we are accessing the private attribute using name mangling:
print(emp2._Employee2__name)
print(emp2._Employee2__salary)
# ? Output:
# ? Jessica
# ? 50000

# We used double underscores (__) in the Employee2 class to trigger name mangling.
# Python internally renames attributes to _ClassName__attribute.
# Although they can still be accessed using this name-mangled form, it is not recommended
# because it breaks encapsulation and relies on the class’s internal implementation.

# Invalid – no standalone global name created for __place due to name mangling (NameError):
# print(_Employee2__place)

# Access instance-shadowed __place:
print(emp2._Employee2__place)  # ? Output: UK

# Access class-level private attribute using name mangling:
print(Employee2._Employee2__place)  # ? Output: India

# Name-mangled access to private attribute (breaks encapsulation):
print(emp2._Employee2__salary)  # ? Output: 50000

# Invalid attribute access (AttributeError):
# print(emp2._Employee2.__place)
# __place is a private attribute and cannot be accessed directly using the class name or instance
# name without name mangling.
